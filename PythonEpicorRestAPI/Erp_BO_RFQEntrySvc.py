import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.RFQEntrySvc
# Description: Request for Quote - Entry
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.RFQEntrySvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.RFQEntrySvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_RFQEntries(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get RFQEntries items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_RFQEntries
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.RFQHeadRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.RFQEntrySvc/RFQEntries",headers=creds) as resp:
           return await resp.json()

async def post_RFQEntries(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_RFQEntries
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.RFQHeadRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.RFQHeadRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.RFQEntrySvc/RFQEntries", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_RFQEntries_Company_RFQNum(Company, RFQNum, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the RFQEntry item
   Description: Calls GetByID to retrieve the RFQEntry item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_RFQEntry
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RFQNum: Desc: RFQNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.RFQHeadRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.RFQEntrySvc/RFQEntries(" + Company + "," + RFQNum + ")",headers=creds) as resp:
           return await resp.json()

async def patch_RFQEntries_Company_RFQNum(Company, RFQNum, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update RFQEntry for the service
   Description: Calls UpdateExt to update RFQEntry. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_RFQEntry
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RFQNum: Desc: RFQNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.RFQHeadRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.RFQEntrySvc/RFQEntries(" + Company + "," + RFQNum + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_RFQEntries_Company_RFQNum(Company, RFQNum, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete RFQEntry item
   Description: Call UpdateExt to delete RFQEntry item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_RFQEntry
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RFQNum: Desc: RFQNum   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.RFQEntrySvc/RFQEntries(" + Company + "," + RFQNum + ")",headers=creds) as resp:
           return await resp.json()

async def get_RFQEntries_Company_RFQNum_RFQItems(Company, RFQNum, select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get RFQItems items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_RFQItems1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RFQNum: Desc: RFQNum   Required: True
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.RFQItemRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.RFQEntrySvc/RFQEntries(" + Company + "," + RFQNum + ")/RFQItems",headers=creds) as resp:
           return await resp.json()

async def get_RFQEntries_Company_RFQNum_RFQItems_Company_RFQNum_RFQLine(Company, RFQNum, RFQLine, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the RFQItem item
   Description: Calls GetByID to retrieve the RFQItem item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_RFQItem1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RFQNum: Desc: RFQNum   Required: True
      :param RFQLine: Desc: RFQLine   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.RFQItemRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.RFQEntrySvc/RFQEntries(" + Company + "," + RFQNum + ")/RFQItems(" + Company + "," + RFQNum + "," + RFQLine + ")",headers=creds) as resp:
           return await resp.json()

async def get_RFQEntries_Company_RFQNum_RFQHeadAttches(Company, RFQNum, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get RFQHeadAttches items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_RFQHeadAttches1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RFQNum: Desc: RFQNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.RFQHeadAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.RFQEntrySvc/RFQEntries(" + Company + "," + RFQNum + ")/RFQHeadAttches",headers=creds) as resp:
           return await resp.json()

async def get_RFQEntries_Company_RFQNum_RFQHeadAttches_Company_RFQNum_DrawingSeq(Company, RFQNum, DrawingSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the RFQHeadAttch item
   Description: Calls GetByID to retrieve the RFQHeadAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_RFQHeadAttch1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RFQNum: Desc: RFQNum   Required: True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.RFQHeadAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.RFQEntrySvc/RFQEntries(" + Company + "," + RFQNum + ")/RFQHeadAttches(" + Company + "," + RFQNum + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_RFQItems(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get RFQItems items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_RFQItems
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.RFQItemRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.RFQEntrySvc/RFQItems",headers=creds) as resp:
           return await resp.json()

async def post_RFQItems(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_RFQItems
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.RFQItemRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.RFQItemRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.RFQEntrySvc/RFQItems", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_RFQItems_Company_RFQNum_RFQLine(Company, RFQNum, RFQLine, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the RFQItem item
   Description: Calls GetByID to retrieve the RFQItem item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_RFQItem
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RFQNum: Desc: RFQNum   Required: True
      :param RFQLine: Desc: RFQLine   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.RFQItemRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.RFQEntrySvc/RFQItems(" + Company + "," + RFQNum + "," + RFQLine + ")",headers=creds) as resp:
           return await resp.json()

async def patch_RFQItems_Company_RFQNum_RFQLine(Company, RFQNum, RFQLine, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update RFQItem for the service
   Description: Calls UpdateExt to update RFQItem. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_RFQItem
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RFQNum: Desc: RFQNum   Required: True
      :param RFQLine: Desc: RFQLine   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.RFQItemRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.RFQEntrySvc/RFQItems(" + Company + "," + RFQNum + "," + RFQLine + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_RFQItems_Company_RFQNum_RFQLine(Company, RFQNum, RFQLine, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete RFQItem item
   Description: Call UpdateExt to delete RFQItem item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_RFQItem
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RFQNum: Desc: RFQNum   Required: True
      :param RFQLine: Desc: RFQLine   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.RFQEntrySvc/RFQItems(" + Company + "," + RFQNum + "," + RFQLine + ")",headers=creds) as resp:
           return await resp.json()

async def get_RFQItems_Company_RFQNum_RFQLine_RFQParts(Company, RFQNum, RFQLine, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get RFQParts items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_RFQParts1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RFQNum: Desc: RFQNum   Required: True
      :param RFQLine: Desc: RFQLine   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.RFQPartRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.RFQEntrySvc/RFQItems(" + Company + "," + RFQNum + "," + RFQLine + ")/RFQParts",headers=creds) as resp:
           return await resp.json()

async def get_RFQItems_Company_RFQNum_RFQLine_RFQParts_Company_RFQNum_RFQLine_MfgNum_MfgPartNum(Company, RFQNum, RFQLine, MfgNum, MfgPartNum, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the RFQPart item
   Description: Calls GetByID to retrieve the RFQPart item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_RFQPart1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RFQNum: Desc: RFQNum   Required: True
      :param RFQLine: Desc: RFQLine   Required: True
      :param MfgNum: Desc: MfgNum   Required: True
      :param MfgPartNum: Desc: MfgPartNum   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.RFQPartRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.RFQEntrySvc/RFQItems(" + Company + "," + RFQNum + "," + RFQLine + ")/RFQParts(" + Company + "," + RFQNum + "," + RFQLine + "," + MfgNum + "," + MfgPartNum + ")",headers=creds) as resp:
           return await resp.json()

async def get_RFQItems_Company_RFQNum_RFQLine_RFQQties(Company, RFQNum, RFQLine, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get RFQQties items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_RFQQties1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RFQNum: Desc: RFQNum   Required: True
      :param RFQLine: Desc: RFQLine   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.RFQQtyRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.RFQEntrySvc/RFQItems(" + Company + "," + RFQNum + "," + RFQLine + ")/RFQQties",headers=creds) as resp:
           return await resp.json()

async def get_RFQItems_Company_RFQNum_RFQLine_RFQQties_Company_RFQNum_RFQLine_QtyNum(Company, RFQNum, RFQLine, QtyNum, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the RFQQty item
   Description: Calls GetByID to retrieve the RFQQty item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_RFQQty1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RFQNum: Desc: RFQNum   Required: True
      :param RFQLine: Desc: RFQLine   Required: True
      :param QtyNum: Desc: QtyNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.RFQQtyRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.RFQEntrySvc/RFQItems(" + Company + "," + RFQNum + "," + RFQLine + ")/RFQQties(" + Company + "," + RFQNum + "," + RFQLine + "," + QtyNum + ")",headers=creds) as resp:
           return await resp.json()

async def get_RFQItems_Company_RFQNum_RFQLine_RFQSourcings(Company, RFQNum, RFQLine, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get RFQSourcings items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_RFQSourcings1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RFQNum: Desc: RFQNum   Required: True
      :param RFQLine: Desc: RFQLine   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.RFQSourcingRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.RFQEntrySvc/RFQItems(" + Company + "," + RFQNum + "," + RFQLine + ")/RFQSourcings",headers=creds) as resp:
           return await resp.json()

async def get_RFQItems_Company_RFQNum_RFQLine_RFQSourcings_Company_RFQNum_RFQLine_SourcingSeq(Company, RFQNum, RFQLine, SourcingSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the RFQSourcing item
   Description: Calls GetByID to retrieve the RFQSourcing item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_RFQSourcing1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RFQNum: Desc: RFQNum   Required: True
      :param RFQLine: Desc: RFQLine   Required: True
      :param SourcingSeq: Desc: SourcingSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.RFQSourcingRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.RFQEntrySvc/RFQItems(" + Company + "," + RFQNum + "," + RFQLine + ")/RFQSourcings(" + Company + "," + RFQNum + "," + RFQLine + "," + SourcingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_RFQItems_Company_RFQNum_RFQLine_RFQVends(Company, RFQNum, RFQLine, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get RFQVends items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_RFQVends1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RFQNum: Desc: RFQNum   Required: True
      :param RFQLine: Desc: RFQLine   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.RFQVendRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.RFQEntrySvc/RFQItems(" + Company + "," + RFQNum + "," + RFQLine + ")/RFQVends",headers=creds) as resp:
           return await resp.json()

async def get_RFQItems_Company_RFQNum_RFQLine_RFQVends_Company_RFQNum_RFQLine_VendorNum_PurPoint(Company, RFQNum, RFQLine, VendorNum, PurPoint, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the RFQVend item
   Description: Calls GetByID to retrieve the RFQVend item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_RFQVend1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RFQNum: Desc: RFQNum   Required: True
      :param RFQLine: Desc: RFQLine   Required: True
      :param VendorNum: Desc: VendorNum   Required: True
      :param PurPoint: Desc: PurPoint   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.RFQVendRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.RFQEntrySvc/RFQItems(" + Company + "," + RFQNum + "," + RFQLine + ")/RFQVends(" + Company + "," + RFQNum + "," + RFQLine + "," + VendorNum + "," + PurPoint + ")",headers=creds) as resp:
           return await resp.json()

async def get_RFQItems_Company_RFQNum_RFQLine_RFQItemAttches(Company, RFQNum, RFQLine, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get RFQItemAttches items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_RFQItemAttches1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RFQNum: Desc: RFQNum   Required: True
      :param RFQLine: Desc: RFQLine   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.RFQItemAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.RFQEntrySvc/RFQItems(" + Company + "," + RFQNum + "," + RFQLine + ")/RFQItemAttches",headers=creds) as resp:
           return await resp.json()

async def get_RFQItems_Company_RFQNum_RFQLine_RFQItemAttches_Company_RFQNum_RFQLine_DrawingSeq(Company, RFQNum, RFQLine, DrawingSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the RFQItemAttch item
   Description: Calls GetByID to retrieve the RFQItemAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_RFQItemAttch1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RFQNum: Desc: RFQNum   Required: True
      :param RFQLine: Desc: RFQLine   Required: True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.RFQItemAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.RFQEntrySvc/RFQItems(" + Company + "," + RFQNum + "," + RFQLine + ")/RFQItemAttches(" + Company + "," + RFQNum + "," + RFQLine + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_RFQParts(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get RFQParts items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_RFQParts
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.RFQPartRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.RFQEntrySvc/RFQParts",headers=creds) as resp:
           return await resp.json()

async def post_RFQParts(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_RFQParts
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.RFQPartRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.RFQPartRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.RFQEntrySvc/RFQParts", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_RFQParts_Company_RFQNum_RFQLine_MfgNum_MfgPartNum(Company, RFQNum, RFQLine, MfgNum, MfgPartNum, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the RFQPart item
   Description: Calls GetByID to retrieve the RFQPart item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_RFQPart
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RFQNum: Desc: RFQNum   Required: True
      :param RFQLine: Desc: RFQLine   Required: True
      :param MfgNum: Desc: MfgNum   Required: True
      :param MfgPartNum: Desc: MfgPartNum   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.RFQPartRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.RFQEntrySvc/RFQParts(" + Company + "," + RFQNum + "," + RFQLine + "," + MfgNum + "," + MfgPartNum + ")",headers=creds) as resp:
           return await resp.json()

async def patch_RFQParts_Company_RFQNum_RFQLine_MfgNum_MfgPartNum(Company, RFQNum, RFQLine, MfgNum, MfgPartNum, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update RFQPart for the service
   Description: Calls UpdateExt to update RFQPart. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_RFQPart
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RFQNum: Desc: RFQNum   Required: True
      :param RFQLine: Desc: RFQLine   Required: True
      :param MfgNum: Desc: MfgNum   Required: True
      :param MfgPartNum: Desc: MfgPartNum   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.RFQPartRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.RFQEntrySvc/RFQParts(" + Company + "," + RFQNum + "," + RFQLine + "," + MfgNum + "," + MfgPartNum + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_RFQParts_Company_RFQNum_RFQLine_MfgNum_MfgPartNum(Company, RFQNum, RFQLine, MfgNum, MfgPartNum, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete RFQPart item
   Description: Call UpdateExt to delete RFQPart item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_RFQPart
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RFQNum: Desc: RFQNum   Required: True
      :param RFQLine: Desc: RFQLine   Required: True
      :param MfgNum: Desc: MfgNum   Required: True
      :param MfgPartNum: Desc: MfgPartNum   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.RFQEntrySvc/RFQParts(" + Company + "," + RFQNum + "," + RFQLine + "," + MfgNum + "," + MfgPartNum + ")",headers=creds) as resp:
           return await resp.json()

async def get_RFQQties(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get RFQQties items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_RFQQties
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.RFQQtyRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.RFQEntrySvc/RFQQties",headers=creds) as resp:
           return await resp.json()

async def post_RFQQties(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_RFQQties
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.RFQQtyRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.RFQQtyRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.RFQEntrySvc/RFQQties", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_RFQQties_Company_RFQNum_RFQLine_QtyNum(Company, RFQNum, RFQLine, QtyNum, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the RFQQty item
   Description: Calls GetByID to retrieve the RFQQty item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_RFQQty
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RFQNum: Desc: RFQNum   Required: True
      :param RFQLine: Desc: RFQLine   Required: True
      :param QtyNum: Desc: QtyNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.RFQQtyRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.RFQEntrySvc/RFQQties(" + Company + "," + RFQNum + "," + RFQLine + "," + QtyNum + ")",headers=creds) as resp:
           return await resp.json()

async def patch_RFQQties_Company_RFQNum_RFQLine_QtyNum(Company, RFQNum, RFQLine, QtyNum, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update RFQQty for the service
   Description: Calls UpdateExt to update RFQQty. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_RFQQty
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RFQNum: Desc: RFQNum   Required: True
      :param RFQLine: Desc: RFQLine   Required: True
      :param QtyNum: Desc: QtyNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.RFQQtyRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.RFQEntrySvc/RFQQties(" + Company + "," + RFQNum + "," + RFQLine + "," + QtyNum + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_RFQQties_Company_RFQNum_RFQLine_QtyNum(Company, RFQNum, RFQLine, QtyNum, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete RFQQty item
   Description: Call UpdateExt to delete RFQQty item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_RFQQty
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RFQNum: Desc: RFQNum   Required: True
      :param RFQLine: Desc: RFQLine   Required: True
      :param QtyNum: Desc: QtyNum   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.RFQEntrySvc/RFQQties(" + Company + "," + RFQNum + "," + RFQLine + "," + QtyNum + ")",headers=creds) as resp:
           return await resp.json()

async def get_RFQSourcings(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get RFQSourcings items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_RFQSourcings
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.RFQSourcingRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.RFQEntrySvc/RFQSourcings",headers=creds) as resp:
           return await resp.json()

async def post_RFQSourcings(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_RFQSourcings
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.RFQSourcingRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.RFQSourcingRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.RFQEntrySvc/RFQSourcings", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_RFQSourcings_Company_RFQNum_RFQLine_SourcingSeq(Company, RFQNum, RFQLine, SourcingSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the RFQSourcing item
   Description: Calls GetByID to retrieve the RFQSourcing item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_RFQSourcing
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RFQNum: Desc: RFQNum   Required: True
      :param RFQLine: Desc: RFQLine   Required: True
      :param SourcingSeq: Desc: SourcingSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.RFQSourcingRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.RFQEntrySvc/RFQSourcings(" + Company + "," + RFQNum + "," + RFQLine + "," + SourcingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_RFQSourcings_Company_RFQNum_RFQLine_SourcingSeq(Company, RFQNum, RFQLine, SourcingSeq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update RFQSourcing for the service
   Description: Calls UpdateExt to update RFQSourcing. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_RFQSourcing
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RFQNum: Desc: RFQNum   Required: True
      :param RFQLine: Desc: RFQLine   Required: True
      :param SourcingSeq: Desc: SourcingSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.RFQSourcingRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.RFQEntrySvc/RFQSourcings(" + Company + "," + RFQNum + "," + RFQLine + "," + SourcingSeq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_RFQSourcings_Company_RFQNum_RFQLine_SourcingSeq(Company, RFQNum, RFQLine, SourcingSeq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete RFQSourcing item
   Description: Call UpdateExt to delete RFQSourcing item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_RFQSourcing
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RFQNum: Desc: RFQNum   Required: True
      :param RFQLine: Desc: RFQLine   Required: True
      :param SourcingSeq: Desc: SourcingSeq   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.RFQEntrySvc/RFQSourcings(" + Company + "," + RFQNum + "," + RFQLine + "," + SourcingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_RFQVends(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get RFQVends items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_RFQVends
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.RFQVendRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.RFQEntrySvc/RFQVends",headers=creds) as resp:
           return await resp.json()

async def post_RFQVends(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_RFQVends
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.RFQVendRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.RFQVendRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.RFQEntrySvc/RFQVends", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_RFQVends_Company_RFQNum_RFQLine_VendorNum_PurPoint(Company, RFQNum, RFQLine, VendorNum, PurPoint, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the RFQVend item
   Description: Calls GetByID to retrieve the RFQVend item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_RFQVend
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RFQNum: Desc: RFQNum   Required: True
      :param RFQLine: Desc: RFQLine   Required: True
      :param VendorNum: Desc: VendorNum   Required: True
      :param PurPoint: Desc: PurPoint   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.RFQVendRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.RFQEntrySvc/RFQVends(" + Company + "," + RFQNum + "," + RFQLine + "," + VendorNum + "," + PurPoint + ")",headers=creds) as resp:
           return await resp.json()

async def patch_RFQVends_Company_RFQNum_RFQLine_VendorNum_PurPoint(Company, RFQNum, RFQLine, VendorNum, PurPoint, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update RFQVend for the service
   Description: Calls UpdateExt to update RFQVend. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_RFQVend
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RFQNum: Desc: RFQNum   Required: True
      :param RFQLine: Desc: RFQLine   Required: True
      :param VendorNum: Desc: VendorNum   Required: True
      :param PurPoint: Desc: PurPoint   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.RFQVendRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.RFQEntrySvc/RFQVends(" + Company + "," + RFQNum + "," + RFQLine + "," + VendorNum + "," + PurPoint + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_RFQVends_Company_RFQNum_RFQLine_VendorNum_PurPoint(Company, RFQNum, RFQLine, VendorNum, PurPoint, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete RFQVend item
   Description: Call UpdateExt to delete RFQVend item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_RFQVend
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RFQNum: Desc: RFQNum   Required: True
      :param RFQLine: Desc: RFQLine   Required: True
      :param VendorNum: Desc: VendorNum   Required: True
      :param PurPoint: Desc: PurPoint   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.RFQEntrySvc/RFQVends(" + Company + "," + RFQNum + "," + RFQLine + "," + VendorNum + "," + PurPoint + ")",headers=creds) as resp:
           return await resp.json()

async def get_RFQItemAttches(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get RFQItemAttches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_RFQItemAttches
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.RFQItemAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.RFQEntrySvc/RFQItemAttches",headers=creds) as resp:
           return await resp.json()

async def post_RFQItemAttches(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_RFQItemAttches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.RFQItemAttchRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.RFQItemAttchRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.RFQEntrySvc/RFQItemAttches", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_RFQItemAttches_Company_RFQNum_RFQLine_DrawingSeq(Company, RFQNum, RFQLine, DrawingSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the RFQItemAttch item
   Description: Calls GetByID to retrieve the RFQItemAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_RFQItemAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RFQNum: Desc: RFQNum   Required: True
      :param RFQLine: Desc: RFQLine   Required: True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.RFQItemAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.RFQEntrySvc/RFQItemAttches(" + Company + "," + RFQNum + "," + RFQLine + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_RFQItemAttches_Company_RFQNum_RFQLine_DrawingSeq(Company, RFQNum, RFQLine, DrawingSeq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update RFQItemAttch for the service
   Description: Calls UpdateExt to update RFQItemAttch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_RFQItemAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RFQNum: Desc: RFQNum   Required: True
      :param RFQLine: Desc: RFQLine   Required: True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.RFQItemAttchRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.RFQEntrySvc/RFQItemAttches(" + Company + "," + RFQNum + "," + RFQLine + "," + DrawingSeq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_RFQItemAttches_Company_RFQNum_RFQLine_DrawingSeq(Company, RFQNum, RFQLine, DrawingSeq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete RFQItemAttch item
   Description: Call UpdateExt to delete RFQItemAttch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_RFQItemAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RFQNum: Desc: RFQNum   Required: True
      :param RFQLine: Desc: RFQLine   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.RFQEntrySvc/RFQItemAttches(" + Company + "," + RFQNum + "," + RFQLine + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_RFQHeadAttches(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get RFQHeadAttches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_RFQHeadAttches
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.RFQHeadAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.RFQEntrySvc/RFQHeadAttches",headers=creds) as resp:
           return await resp.json()

async def post_RFQHeadAttches(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_RFQHeadAttches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.RFQHeadAttchRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.RFQHeadAttchRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.RFQEntrySvc/RFQHeadAttches", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_RFQHeadAttches_Company_RFQNum_DrawingSeq(Company, RFQNum, DrawingSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the RFQHeadAttch item
   Description: Calls GetByID to retrieve the RFQHeadAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_RFQHeadAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RFQNum: Desc: RFQNum   Required: True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.RFQHeadAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.RFQEntrySvc/RFQHeadAttches(" + Company + "," + RFQNum + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_RFQHeadAttches_Company_RFQNum_DrawingSeq(Company, RFQNum, DrawingSeq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update RFQHeadAttch for the service
   Description: Calls UpdateExt to update RFQHeadAttch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_RFQHeadAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RFQNum: Desc: RFQNum   Required: True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.RFQHeadAttchRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.RFQEntrySvc/RFQHeadAttches(" + Company + "," + RFQNum + "," + DrawingSeq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_RFQHeadAttches_Company_RFQNum_DrawingSeq(Company, RFQNum, DrawingSeq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete RFQHeadAttch item
   Description: Call UpdateExt to delete RFQHeadAttch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_RFQHeadAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RFQNum: Desc: RFQNum   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.RFQEntrySvc/RFQHeadAttches(" + Company + "," + RFQNum + "," + DrawingSeq + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.RFQHeadListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.RFQEntrySvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseRFQHead, whereClauseRFQHeadAttch, whereClauseRFQItem, whereClauseRFQItemAttch, whereClauseRFQPart, whereClauseRFQQty, whereClauseRFQSourcing, whereClauseRFQVend, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClauseRFQHead=" + whereClauseRFQHead
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseRFQHeadAttch=" + whereClauseRFQHeadAttch
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseRFQItem=" + whereClauseRFQItem
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseRFQItemAttch=" + whereClauseRFQItemAttch
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseRFQPart=" + whereClauseRFQPart
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseRFQQty=" + whereClauseRFQQty
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseRFQSourcing=" + whereClauseRFQSourcing
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseRFQVend=" + whereClauseRFQVend
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.RFQEntrySvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(rfQNum, epicorHeaders = None):
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
   params += "rfQNum=" + rfQNum

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.RFQEntrySvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.RFQEntrySvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_AddRFQItemFromJob(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method AddRFQItemFromJob
   Description: This method adds RFQItem from Job
   OperationID: AddRFQItemFromJob
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/AddRFQItemFromJob_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AddRFQItemFromJob_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.RFQEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_AddRFQItemFromMiscReq(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method AddRFQItemFromMiscReq
   Description: This method adds RFQItem from RFQSugg created from non-job requisitions
   OperationID: AddRFQItemFromMiscReq
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/AddRFQItemFromMiscReq_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AddRFQItemFromMiscReq_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.RFQEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_AddRFQItemFromQuote(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method AddRFQItemFromQuote
   Description: This method adds RFQItem from Qoute
   OperationID: AddRFQItemFromQuote
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/AddRFQItemFromQuote_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AddRFQItemFromQuote_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.RFQEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_AddRFQItemJob(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method AddRFQItemJob
   Description: This method adds RFQItem with SugNumList
   OperationID: AddRFQItemJob
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/AddRFQItemJob_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AddRFQItemJob_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.RFQEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_AddRFQItemMiscReq(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method AddRFQItemMiscReq
   Description: This method adds RFQItem with SugNumList from non-job related requisitions
   OperationID: AddRFQItemMiscReq
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/AddRFQItemMiscReq_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AddRFQItemMiscReq_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.RFQEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_AddRFQItemQuote(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method AddRFQItemQuote
   Description: This method adds RFQItem with SugNumList from Qoute
   OperationID: AddRFQItemQuote
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/AddRFQItemQuote_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AddRFQItemQuote_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.RFQEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_AddSupplierFromSearch(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method AddSupplierFromSearch
   Description: Call this method when UI uses Add (search).
   OperationID: AddSupplierFromSearch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/AddSupplierFromSearch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AddSupplierFromSearch_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.RFQEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckComplianceFail(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckComplianceFail
   Description: Check for every vendor of the RFQ if it requires to be compliant.
   OperationID: CheckComplianceFail
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckComplianceFail_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckComplianceFail_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.RFQEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CreateNewRFQQty(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CreateNewRFQQty
   Description: Create RFQQty record. Please use this method instead of GetNewRFQQty.
   OperationID: CreateNewRFQQty
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CreateNewRFQQty_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CreateNewRFQQty_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.RFQEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DuplicateRFQ(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DuplicateRFQ
   Description: Duplicates RFQ.
   OperationID: DuplicateRFQ
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DuplicateRFQ_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DuplicateRFQ_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.RFQEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_AddVendorsFromSearch(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method AddVendorsFromSearch
   Description: Duplicates RFQ.
   OperationID: AddVendorsFromSearch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/AddVendorsFromSearch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AddVendorsFromSearch_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.RFQEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetSourcingStatus(epicorHeaders = None):
   """  
   Summary: Invoke method GetSourcingStatus
   OperationID: GetSourcingStatus
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetSourcingStatus_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.RFQEntrySvc/List",headers=creds) as resp:
           return await resp.json()

async def post_OnChangeofBuyerID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeofBuyerID
   Description: Call this method when the value of BuyerID changes.
   OperationID: OnChangeofBuyerID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeofBuyerID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeofBuyerID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.RFQEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangePartNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangePartNum
   Description: Call this method when the value of PartNum changes.
   OperationID: OnChangePartNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangePartNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangePartNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.RFQEntrySvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.RFQEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangePurPoint(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangePurPoint
   Description: Call this method when the value of PurPoint changes.
   OperationID: OnChangePurPoint
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangePurPoint_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangePurPoint_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.RFQEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeRFQItemPUM(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeRFQItemPUM
   Description: Call this method when the value of RFQItem.PUM changes.
   OperationID: OnChangeRFQItemPUM
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeRFQItemPUM_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeRFQItemPUM_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.RFQEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeVendorID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeVendorID
   Description: Call this method when the value of VendorID changes.
   OperationID: OnChangeVendorID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeVendorID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeVendorID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.RFQEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OpenRFQ(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OpenRFQ
   Description: Close/Open the RFQ.
   OperationID: OpenRFQ
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OpenRFQ_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OpenRFQ_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.RFQEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ReOpenRFQLine(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ReOpenRFQLine
   Description: Reopens the RFQ line.
   OperationID: ReOpenRFQLine
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ReOpenRFQLine_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ReOpenRFQLine_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.RFQEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_VendorWizard(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method VendorWizard
   Description: This procedures generates a list of potential Vendors for
the RFQItem.PartNum.
   OperationID: VendorWizard
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/VendorWizard_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/VendorWizard_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.RFQEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidateSelectedVendAttributes(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateSelectedVendAttributes
   Description: This procedures called from Kinetic to validate Selected Vendor Attributes
   OperationID: ValidateSelectedVendAttributes
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateSelectedVendAttributes_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateSelectedVendAttributes_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.RFQEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ECCUpdateFinal(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ECCUpdateFinal
   Description: Method specific to ECC.
This is used as a final process using the XML that was sent from the Web.
   OperationID: ECCUpdateFinal
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ECCUpdateFinal_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ECCUpdateFinal_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.RFQEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewRFQHead(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewRFQHead
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewRFQHead
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewRFQHead_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewRFQHead_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.RFQEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewRFQHeadAttch(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewRFQHeadAttch
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewRFQHeadAttch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewRFQHeadAttch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewRFQHeadAttch_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.RFQEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewRFQItem(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewRFQItem
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewRFQItem
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewRFQItem_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewRFQItem_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.RFQEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewRFQItemAttch(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewRFQItemAttch
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewRFQItemAttch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewRFQItemAttch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewRFQItemAttch_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.RFQEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewRFQPart(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewRFQPart
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewRFQPart
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewRFQPart_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewRFQPart_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.RFQEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewRFQQty(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewRFQQty
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewRFQQty
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewRFQQty_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewRFQQty_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.RFQEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewRFQSourcing(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewRFQSourcing
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewRFQSourcing
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewRFQSourcing_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewRFQSourcing_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.RFQEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewRFQVend(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewRFQVend
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewRFQVend
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewRFQVend_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewRFQVend_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.RFQEntrySvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.RFQEntrySvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.RFQEntrySvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.RFQEntrySvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.RFQEntrySvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.RFQEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RFQHeadAttchRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_RFQHeadAttchRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RFQHeadListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_RFQHeadListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RFQHeadRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_RFQHeadRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RFQItemAttchRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_RFQItemAttchRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RFQItemRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_RFQItemRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RFQPartRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_RFQPartRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RFQQtyRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_RFQQtyRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RFQSourcingRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_RFQSourcingRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RFQVendRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_RFQVendRow] = obj["value"]
      pass

class Erp_Tablesets_RFQHeadAttchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.RFQNum:int = obj["RFQNum"]
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

class Erp_Tablesets_RFQHeadListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.OpenRFQ:bool = obj["OpenRFQ"]
      """  Indicates if the RFQ is open or closed. This is set automatically when all the RFQItem records have been closed or can be set if the user voids the RFQ.  This field is not directly maintainable.  """  
      self.RFQNum:int = obj["RFQNum"]
      """  Number that uniquely identifies the RFQ document.  """  
      self.RFQDate:str = obj["RFQDate"]
      """  Date that this RFQ was entered.  """  
      self.RFQDueDate:str = obj["RFQDueDate"]
      """  The date the vendor responses are due.  """  
      self.BuyerID:str = obj["BuyerID"]
      """  The ID that links to the Purchasing Agent master file.  """  
      self.CommentText:str = obj["CommentText"]
      """  Contains comments about the RFQ. These will be printed on the RFQ document.  """  
      self.ReadyToPrint:bool = obj["ReadyToPrint"]
      """  Indicates if the RFQ is to selected for printing during the Mass Print process.  """  
      self.RespondDate:str = obj["RespondDate"]
      """  Date the supplier is to respond by  """  
      self.DecisionDate:str = obj["DecisionDate"]
      """  Date the PO is planned to be awarded  """  
      self.PostToWeb:bool = obj["PostToWeb"]
      """  Indicates the Supplier will respond via Suppliers workbench  """  
      self.PostDate:str = obj["PostDate"]
      """  Date Buyer posted the RFQ  """  
      self.GlbCompany:str = obj["GlbCompany"]
      """  Global Company identifier.  Used in Consolidated Purchasing.  """  
      self.GlbRFQNum:int = obj["GlbRFQNum"]
      """  Global RFQ identifier.  Used in Consolidated Purchasing.  """  
      self.AutoPrintReady:bool = obj["AutoPrintReady"]
      """  Field to use for the BAM to Auto-Print the Crystal Report or Bartender Labels associated to this table.  """  
      self.UOMClassID:str = obj["UOMClassID"]
      """  UOM Class ID  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.WebVendorExists:bool = obj["WebVendorExists"]
      self.BuyerIDName:str = obj["BuyerIDName"]
      """  Name of Purchasing Agent or Group. This is printed on the PO by the authorized signature line.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_RFQHeadRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.OpenRFQ:bool = obj["OpenRFQ"]
      """  Indicates if the RFQ is open or closed. This is set automatically when all the RFQItem records have been closed or can be set if the user voids the RFQ.  This field is not directly maintainable.  """  
      self.RFQNum:int = obj["RFQNum"]
      """  Number that uniquely identifies the RFQ document.  """  
      self.RFQDate:str = obj["RFQDate"]
      """  Date that this RFQ was entered.  """  
      self.RFQDueDate:str = obj["RFQDueDate"]
      """  The date the vendor responses are due.  """  
      self.BuyerID:str = obj["BuyerID"]
      """  The ID that links to the Purchasing Agent master file.  """  
      self.CommentText:str = obj["CommentText"]
      """  Contains comments about the RFQ. These will be printed on the RFQ document.  """  
      self.ReadyToPrint:bool = obj["ReadyToPrint"]
      """  Indicates if the RFQ is to selected for printing during the Mass Print process.  """  
      self.RespondDate:str = obj["RespondDate"]
      """  Date the supplier is to respond by  """  
      self.DecisionDate:str = obj["DecisionDate"]
      """  Date the PO is planned to be awarded  """  
      self.PostToWeb:bool = obj["PostToWeb"]
      """  Indicates the Supplier will respond via Suppliers workbench  """  
      self.PostDate:str = obj["PostDate"]
      """  Date Buyer posted the RFQ  """  
      self.GlbCompany:str = obj["GlbCompany"]
      """  Global Company identifier.  Used in Consolidated Purchasing.  """  
      self.GlbRFQNum:int = obj["GlbRFQNum"]
      """  Global RFQ identifier.  Used in Consolidated Purchasing.  """  
      self.AutoPrintReady:bool = obj["AutoPrintReady"]
      """  Field to use for the BAM to Auto-Print the Crystal Report or Bartender Labels associated to this table.  """  
      self.UOMClassID:str = obj["UOMClassID"]
      """  UOM Class ID  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.WebVendorExists:bool = obj["WebVendorExists"]
      self.BitFlag:int = obj["BitFlag"]
      self.BuyerIDName:str = obj["BuyerIDName"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_RFQItemAttchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.RFQNum:int = obj["RFQNum"]
      self.RFQLine:int = obj["RFQLine"]
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

class Erp_Tablesets_RFQItemRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.OpenItem:bool = obj["OpenItem"]
      """  Indicates if this line item is Open/Closed.  Set to "Closed" as when there are no longer any open RFQDtl records. This can also be closed when the user voids the RFQItem.  """  
      self.RFQNum:int = obj["RFQNum"]
      """  RFQ number  that the item is linked to.  """  
      self.RFQLine:int = obj["RFQLine"]
      """  The line number of this detail record on the RFQ. This number uniquely identifies the record within the RFQ. The number is not directly maintainable, it's assigned by the system when records are created.  """  
      self.LineDesc:str = obj["LineDesc"]
      """   Description of line item.
Defaults from JobOper, JobMtl or Part depending on the reference.  """  
      self.IUM:str = obj["IUM"]
      """  Issue (our) unit of measure.  """  
      self.PartNum:str = obj["PartNum"]
      """  OUR internal part number for this item.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  OUR revision number of the OUR part.  An optional field. Defaults from the most current  PartRev.RevisionNum.  """  
      self.CommentText:str = obj["CommentText"]
      """  Contains comments about the item. These will be printed on the RFQ. Defaults from the Job’s Material Purchasing comments.  """  
      self.ClassID:str = obj["ClassID"]
      """  The foreign key to the PartClass file.  May be blank, if entered must be valid in PartClass file.  Defaulted from Part.ClassID. The PartClass is used in determining a default G/L expense account.  """  
      self.JobNum:str = obj["JobNum"]
      """  Related job number.  """  
      self.QuoteNum:int = obj["QuoteNum"]
      """  Related Customer QuoteNum.  """  
      self.QuoteLine:int = obj["QuoteLine"]
      """  The QuoteLine that record is related to.  """  
      self.ItemType:str = obj["ItemType"]
      """  Mtl = Material, Sub = Subcontract  """  
      self.OpCode:str = obj["OpCode"]
      """   Operation Code - used to identify specific subcontracting operation that is needs to be quoted.
This field can be blank (raw materials) or must be valid in the OpMaster (subcontracts service).  """  
      self.AssemblySeq:int = obj["AssemblySeq"]
      """  Assembly sequence number that this rfq is associated with.  """  
      self.JobSeq:int = obj["JobSeq"]
      """  Job Seq of the requirement. Not maintainable.  """  
      self.RFQVendQuotes:int = obj["RFQVendQuotes"]
      """  The number of vendor quotes that are required for this rfq line.  """  
      self.GlbCompany:str = obj["GlbCompany"]
      """  Global Company identifier.  Used in Consolidated Purchasing.  """  
      self.GlbRFQNum:str = obj["GlbRFQNum"]
      """  Global RFQ identifier.  Used in Consolidated Purchasing.  """  
      self.GlbRFQLine:int = obj["GlbRFQLine"]
      """  Global RFQ Line identifier.  Used in Consolidated Purchasing.  """  
      self.RequiredQty:int = obj["RequiredQty"]
      """  Required Quantity from the source record (JobMtl/JobOper/QuoteMtl/QuoteOpr) used to create PORel.  Not user updatable.  """  
      self.RcvInspectionReq:bool = obj["RcvInspectionReq"]
      """  Indicates if inspection is required when items are received.  Used when create PODetail records  """  
      self.WarehouseCode:str = obj["WarehouseCode"]
      """  The warehouse that the material is allocated against.  """  
      self.SrcVendQuotes:int = obj["SrcVendQuotes"]
      """  Number of quotes required as indicated by the source file  """  
      self.ValidSrc:bool = obj["ValidSrc"]
      """  Indicates if the Source file (JobMtl,QuoteMtl,...) is a valid source record  """  
      self.PUM:str = obj["PUM"]
      """  The Purchase Unit of Measure  """  
      self.PurchasingFactor:int = obj["PurchasingFactor"]
      """  Used to capture the purchasing factor.  """  
      self.PurchasingFactorDirection:str = obj["PurchasingFactorDirection"]
      """  Indicates how Purchasing Factor is used in calculations.  If M (multiply), the Factor is multiplied, if  D (divide) the factor is divided.  """  
      self.ComplianceMsg:str = obj["ComplianceMsg"]
      """  Displays the cause why the item is not compliant.  """  
      self.UOMClassID:str = obj["UOMClassID"]
      """  UOM Class ID  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.ReqNum:int = obj["ReqNum"]
      """  Requisition number that the detail line is linked to.  """  
      self.ReqLine:int = obj["ReqLine"]
      """  The line number of detail record on the requisition.  This number uniquely identifies the record within the Requisition number.  The number is not directly maintainable; it's assigned by the system when records are created.  """  
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.NotCompliant:bool = obj["NotCompliant"]
      """  Indicates if the item on the line is not compliant on its source.  """  
      self.Source:str = obj["Source"]
      self.BitFlag:int = obj["BitFlag"]
      self.AssemblySeqDescription:str = obj["AssemblySeqDescription"]
      self.AttributeSetIDShortDescription:str = obj["AttributeSetIDShortDescription"]
      self.AttributeSetIDDescription:str = obj["AttributeSetIDDescription"]
      self.ClassDescription:str = obj["ClassDescription"]
      self.JobNumPartDescription:str = obj["JobNumPartDescription"]
      self.OpCodeOpDesc:str = obj["OpCodeOpDesc"]
      self.PartNumTrackInventoryAttributes:bool = obj["PartNumTrackInventoryAttributes"]
      self.PartNumAttrClassID:str = obj["PartNumAttrClassID"]
      self.PartNumTrackLots:bool = obj["PartNumTrackLots"]
      self.PartNumPartDescription:str = obj["PartNumPartDescription"]
      self.PartNumSellingFactor:int = obj["PartNumSellingFactor"]
      self.PartNumTrackDimension:bool = obj["PartNumTrackDimension"]
      self.PartNumIUM:str = obj["PartNumIUM"]
      self.PartNumPricePerCode:str = obj["PartNumPricePerCode"]
      self.PartNumSalesUM:str = obj["PartNumSalesUM"]
      self.PartNumTrackSerialNum:bool = obj["PartNumTrackSerialNum"]
      self.PartNumTrackInventoryByRevision:bool = obj["PartNumTrackInventoryByRevision"]
      self.QuoteLineLineDesc:str = obj["QuoteLineLineDesc"]
      self.QuoteNumCurrencyCode:str = obj["QuoteNumCurrencyCode"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_RFQPartRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.RFQNum:int = obj["RFQNum"]
      """  RFQNum  """  
      self.RFQLine:int = obj["RFQLine"]
      """  RFQLine  """  
      self.MfgNum:int = obj["MfgNum"]
      """  MfgNum  """  
      self.MfgPartNum:str = obj["MfgPartNum"]
      """  MfgPartNum  """  
      self.RFQInclude:bool = obj["RFQInclude"]
      """  True if this mfg part should be included on the RFQ, false if it should not be. Defaults to true.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.MfgNumName:str = obj["MfgNumName"]
      self.MfgNumID:str = obj["MfgNumID"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_RFQQtyRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.RFQNum:int = obj["RFQNum"]
      """  Number that uniquely identifies the RFQ document.  """  
      self.RFQLine:int = obj["RFQLine"]
      """  The line number of the detail record on the RFQ. This number uniquely identifies the record within the RFQ. The number not directly maintainable, it's assigned by the system when records are created.  """  
      self.QtyNum:int = obj["QtyNum"]
      """  An internally used integer assigned by the system to provide a unique key to the QuoteQty file. Allowing virtually unlimited quantities to be quoted for each detail line on a quote. This number is assigned as one greater than last one on file for the given QuoteDtl record.  """  
      self.Quantity:int = obj["Quantity"]
      """  The quantity for which the RFQ is requesting a quote.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.DspUOM:str = obj["DspUOM"]
      """  Display only field based on RFQItem.PUM  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RFQLineLineDesc:str = obj["RFQLineLineDesc"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_RFQSourcingRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.RFQNum:int = obj["RFQNum"]
      """  Number that uniquely identifies the RFQ document.  """  
      self.RFQLine:int = obj["RFQLine"]
      """  The line number of this detail record on the RFQ. This number uniquely identifies the record within the RFQ. The number is not directly maintainable, it's assigned by the system when records are created.  """  
      self.SourcingSeq:int = obj["SourcingSeq"]
      """  Sequence number used to complete the primary index and in case more than one records get created.  """  
      self.SourcingID:str = obj["SourcingID"]
      """  ID number that Sorcing retrieves in order to keep track of an auction.  """  
      self.SourcingStatus:str = obj["SourcingStatus"]
      """  Status of the Auction ( S = Send to Sourcing , P = Posted to Sourcing and Empty, Blank = Available to be sent)  """  
      self.AuctionTitle:str = obj["AuctionTitle"]
      """  Title of the auction  """  
      self.BidAnonimity:str = obj["BidAnonimity"]
      """  An option that restricts the information displayed about the winner of the event.  """  
      self.Category:str = obj["Category"]
      """  Category in which the items belong  """  
      self.Duration:int = obj["Duration"]
      """  The number of hours that the auction will stay online and open for bids  """  
      self.EventType:str = obj["EventType"]
      """  Type of Event Auction  """  
      self.ItemDescription:str = obj["ItemDescription"]
      """  Description of the item that is being sold / bought  """  
      self.MinOfferDec:int = obj["MinOfferDec"]
      """  Minimum Offer Decrement. The minimum amount of money that one user can bid over the current price.  """  
      self.PreviewDate:str = obj["PreviewDate"]
      """  Preview time is a given time for the users to preview the auction without being able to make bids yet.  """  
      self.PreviewTime:int = obj["PreviewTime"]
      """  Displays the time at which the auction can be previewed.  """  
      self.StartingDate:str = obj["StartingDate"]
      """  Start date is the date when the auction will be available for users to make bids.  """  
      self.StartingTime:int = obj["StartingTime"]
      """  Starting time for the users to be able to make bids.  """  
      self.ExpectedTotalPrice:int = obj["ExpectedTotalPrice"]
      """  Expected Total Price  """  
      self.ActualTotalPrice:int = obj["ActualTotalPrice"]
      """  Actual Total Price  """  
      self.AnonimityLevel:str = obj["AnonimityLevel"]
      """  Anonimity Level. Level of restriction for the information displayed about the winner of the event.  """  
      self.NegativeBids:bool = obj["NegativeBids"]
      """  Strictly speaking, negative bidding is simply placing a bid using a negative number.  """  
      self.UOMCode:str = obj["UOMCode"]
      """  Unit of Measure (used only on Dynamic Descent Events)  """  
      self.UnitQty:int = obj["UnitQty"]
      """  When creating a dynamic ascending or dynamic descending event you must enter the number of units you wish to buy or sell.  """  
      self.DecisionMakingRule:str = obj["DecisionMakingRule"]
      """  A rule that can determine how the winner of an event is selected.  """  
      self.StartingPrice:int = obj["StartingPrice"]
      """  The beginning or opening price of an item or service in a Dutch or reverse Dutch event.  """  
      self.MaxPrice:int = obj["MaxPrice"]
      """  The highest price a buyer will pay for an evented item.  """  
      self.PriceIncrement:int = obj["PriceIncrement"]
      """  Price Increment at each Interval. Used in buyer-centric events, it is the amount by which an event price increases per each interval of time.  """  
      self.TimeInterval:int = obj["TimeInterval"]
      """  Time Interval for each Price Increase  """  
      self.UNSPSC:str = obj["UNSPSC"]
      """  Universal Standard Products and Services Classification (UNSPSC)  """  
      self.FormsOfPayment:str = obj["FormsOfPayment"]
      """  Forms Of Payment  """  
      self.FreeOnBoard:str = obj["FreeOnBoard"]
      """  Designates who pays the carrier for the shipping of an item  """  
      self.Terms:str = obj["Terms"]
      """  The payment terms of a posting.  """  
      self.ShippingOptions:str = obj["ShippingOptions"]
      """  The various methods of shipping that apply to a posting.  """  
      self.Location:str = obj["Location"]
      """  The geographic location of an item for sale, or, in the case of an item for purchase, the geographic location where the item should be delivered.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.StartingTimeString:str = obj["StartingTimeString"]
      """  String representation of the StartingTime field  """  
      self.PreviewTimeString:str = obj["PreviewTimeString"]
      """  String representation of the Preview Time field  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_RFQVendRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.OpenItem:bool = obj["OpenItem"]
      """  Indicates if this line item is Open/Closed. Gets set to "Closed" when there are no longer any open RFQDtl records. This can also be closed when the user voids the RFQItem.  """  
      self.Response:str = obj["Response"]
      """   Indicates if the vendor has responded. This field is not directly maintainable, when price breaks are entered this is set to yes.
Valid values are 
 "W" = WAITING for response,
 "R" = response RECEIVED, and
 "N" = NO response RECEIVED, nor are we waiting for one.  """  
      self.RFQNum:int = obj["RFQNum"]
      """  RFQ number  that the item is linked to.  """  
      self.RFQLine:int = obj["RFQLine"]
      """  The line number of the detail record on the RFQ. This number uniquely identifies the record within the RFQ. The number is not directly maintainable, it's assigned by the system when records are created.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  Vendor's unique internal number.  """  
      self.PurPoint:str = obj["PurPoint"]
      """  Vendor Purchase Point ID.  """  
      self.ConNum:int = obj["ConNum"]
      """  Supplier contact linked to this RFQ  """  
      self.RespondVia:str = obj["RespondVia"]
      """  Can be "Web" or "Client"  """  
      self.RespondDate:str = obj["RespondDate"]
      """  Date Supplier responded to the RFQ.  Only used when the response came from the Web.  """  
      self.ComplianceMsg:str = obj["ComplianceMsg"]
      """  Compliance Message  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.VendorID:str = obj["VendorID"]
      self.VendorName:str = obj["VendorName"]
      self.OpenRFQ:bool = obj["OpenRFQ"]
      self.LineDescription:str = obj["LineDescription"]
      self.PartNum:str = obj["PartNum"]
      self.RevisionNum:str = obj["RevisionNum"]
      self.JobNum:str = obj["JobNum"]
      self.QuoteNum:int = obj["QuoteNum"]
      self.OpCode:str = obj["OpCode"]
      self.OpDescription:str = obj["OpDescription"]
      self.ResponseDescription:str = obj["ResponseDescription"]
      self.EffectiveDate:str = obj["EffectiveDate"]
      """  Vend Part Effective Date  """  
      self.RFQSource:str = obj["RFQSource"]
      """  Description of the Source field (either Job, Quote or blank)  """  
      self.RFQStatus:str = obj["RFQStatus"]
      self.BuyerID:str = obj["BuyerID"]
      """  Buyer Name  """  
      self.RFQDate:str = obj["RFQDate"]
      self.RFQDueDate:str = obj["RFQDueDate"]
      self.OurUOM:str = obj["OurUOM"]
      """  Our UOM  """  
      self.SupplierUOM:str = obj["SupplierUOM"]
      """  Supplier UOM  """  
      self.IUM:str = obj["IUM"]
      """  Base UOM Code from Part Master  """  
      self.PUM:str = obj["PUM"]
      """  The Purchasing Unit of measure for the Part.  """  
      self.CalcOurQty:int = obj["CalcOurQty"]
      self.CalcVendQty:int = obj["CalcVendQty"]
      self.NotCompliant:bool = obj["NotCompliant"]
      """  Indicates if the item on the line is not compliant on its source.  """  
      self.Selected:bool = obj["Selected"]
      self.AddressFormatted:str = obj["AddressFormatted"]
      """  Supplier Address  """  
      self.ResponseOptions:str = obj["ResponseOptions"]
      """  Valid Response options for combo.  """  
      self.AttributeDescription:str = obj["AttributeDescription"]
      self.AttributeSetID:int = obj["AttributeSetID"]
      self.AttributeShortDescription:str = obj["AttributeShortDescription"]
      self.BitFlag:int = obj["BitFlag"]
      self.RFQLineLineDesc:str = obj["RFQLineLineDesc"]
      self.VendorNumVendorID:str = obj["VendorNumVendorID"]
      self.VendorNumAddress2:str = obj["VendorNumAddress2"]
      self.VendorNumName:str = obj["VendorNumName"]
      self.VendorNumCountry:str = obj["VendorNumCountry"]
      self.VendorNumCity:str = obj["VendorNumCity"]
      self.VendorNumZIP:str = obj["VendorNumZIP"]
      self.VendorNumTermsCode:str = obj["VendorNumTermsCode"]
      self.VendorNumAddress3:str = obj["VendorNumAddress3"]
      self.VendorNumCurrencyCode:str = obj["VendorNumCurrencyCode"]
      self.VendorNumAddress1:str = obj["VendorNumAddress1"]
      self.VendorNumState:str = obj["VendorNumState"]
      self.VendorNumDefaultFOB:str = obj["VendorNumDefaultFOB"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class AddRFQItemFromJob_input:
   """ Required : 
   piRFQNum
   pcJobNum
   pcGlbCompany
   ds
   """  
   def __init__(self, obj):
      self.piRFQNum:int = obj["piRFQNum"]
      """  RFQ Number  """  
      self.pcJobNum:str = obj["pcJobNum"]
      """  Job Number  """  
      self.pcGlbCompany:str = obj["pcGlbCompany"]
      """  GlbCompany Number  """  
      self.ds:list[Erp_Tablesets_RFQEntryTableset] = obj["ds"]
      pass

class AddRFQItemFromJob_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_RFQEntryTableset] = obj["ds"]
      self.pcMessage:str = obj["parameters"]
      pass

      """  output parameters  """  

class AddRFQItemFromMiscReq_input:
   """ Required : 
   piRFQNum
   pcGlbCompany
   ds
   """  
   def __init__(self, obj):
      self.piRFQNum:int = obj["piRFQNum"]
      """  RFQ Number  """  
      self.pcGlbCompany:str = obj["pcGlbCompany"]
      """  GlbCompany Number  """  
      self.ds:list[Erp_Tablesets_RFQEntryTableset] = obj["ds"]
      pass

class AddRFQItemFromMiscReq_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_RFQEntryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class AddRFQItemFromQuote_input:
   """ Required : 
   piRFQNum
   piQuoteNum
   pcGlbCompany
   ds
   """  
   def __init__(self, obj):
      self.piRFQNum:int = obj["piRFQNum"]
      """  RFQ Number  """  
      self.piQuoteNum:int = obj["piQuoteNum"]
      """  Quote Number  """  
      self.pcGlbCompany:str = obj["pcGlbCompany"]
      """  GlbCompany Number  """  
      self.ds:list[Erp_Tablesets_RFQEntryTableset] = obj["ds"]
      pass

class AddRFQItemFromQuote_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_RFQEntryTableset] = obj["ds"]
      self.pcMessage:str = obj["parameters"]
      pass

      """  output parameters  """  

class AddRFQItemJob_input:
   """ Required : 
   piRFQNum
   pcSugNumList
   ds
   """  
   def __init__(self, obj):
      self.piRFQNum:int = obj["piRFQNum"]
      """  RFQ Number  """  
      self.pcSugNumList:str = obj["pcSugNumList"]
      """  SugNumList  """  
      self.ds:list[Erp_Tablesets_RFQEntryTableset] = obj["ds"]
      pass

class AddRFQItemJob_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_RFQEntryTableset] = obj["ds"]
      self.pcMessage:str = obj["parameters"]
      pass

      """  output parameters  """  

class AddRFQItemMiscReq_input:
   """ Required : 
   piRFQNum
   pcSugNumList
   ds
   """  
   def __init__(self, obj):
      self.piRFQNum:int = obj["piRFQNum"]
      """  RFQ Number  """  
      self.pcSugNumList:str = obj["pcSugNumList"]
      """  SugNumList  """  
      self.ds:list[Erp_Tablesets_RFQEntryTableset] = obj["ds"]
      pass

class AddRFQItemMiscReq_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_RFQEntryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class AddRFQItemQuote_input:
   """ Required : 
   pcSugNumList
   piRFQNum
   ds
   """  
   def __init__(self, obj):
      self.pcSugNumList:str = obj["pcSugNumList"]
      """  SugNumList  """  
      self.piRFQNum:int = obj["piRFQNum"]
      """  RFQ Number  """  
      self.ds:list[Erp_Tablesets_RFQEntryTableset] = obj["ds"]
      pass

class AddRFQItemQuote_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_RFQEntryTableset] = obj["ds"]
      self.pcMessage:str = obj["parameters"]
      pass

      """  output parameters  """  

class AddSupplierFromSearch_input:
   """ Required : 
   ds
   pcVendorID
   pcPurPoint
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_RFQEntryTableset] = obj["ds"]
      self.pcVendorID:str = obj["pcVendorID"]
      """  VendorID  """  
      self.pcPurPoint:str = obj["pcPurPoint"]
      """  PurPoint  """  
      pass

class AddSupplierFromSearch_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_RFQEntryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class AddVendorsFromSearch_input:
   """ Required : 
   ds
   vendNumList
   vendPPList
   rfqNum
   rfqLine
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_RFQEntryTableset] = obj["ds"]
      self.vendNumList:str = obj["vendNumList"]
      """  List of Vendor Numbers  """  
      self.vendPPList:str = obj["vendPPList"]
      """  List of Vendor Purchase Point  """  
      self.rfqNum:int = obj["rfqNum"]
      """  RFQ Number  """  
      self.rfqLine:int = obj["rfqLine"]
      """  RFQ Line Number  """  
      pass

class AddVendorsFromSearch_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_RFQEntryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class CheckComplianceFail_input:
   """ Required : 
   rfqNum
   rfqLine
   vendorNum
   purPoint
   """  
   def __init__(self, obj):
      self.rfqNum:int = obj["rfqNum"]
      """  Current RFQ.  """  
      self.rfqLine:int = obj["rfqLine"]
      """  Current RFQ Line.  """  
      self.vendorNum:int = obj["vendorNum"]
      """  Current Vendor.  """  
      self.purPoint:str = obj["purPoint"]
      """  Current Purchase Point.  """  
      pass

class CheckComplianceFail_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.compliant:bool = obj["compliant"]
      pass

      """  output parameters  """  

class CreateNewRFQQty_input:
   """ Required : 
   ds
   rfqNum
   rfqLine
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_RFQEntryTableset] = obj["ds"]
      self.rfqNum:int = obj["rfqNum"]
      """  RFQ Number  """  
      self.rfqLine:int = obj["rfqLine"]
      """  RFQ Line Number  """  
      pass

class CreateNewRFQQty_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_RFQEntryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class DeleteByID_input:
   """ Required : 
   rfQNum
   """  
   def __init__(self, obj):
      self.rfQNum:int = obj["rfQNum"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class DuplicateRFQ_input:
   """ Required : 
   piSourceRFQNum
   """  
   def __init__(self, obj):
      self.piSourceRFQNum:int = obj["piSourceRFQNum"]
      """  Source RFQ Number  """  
      pass

class DuplicateRFQ_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_RFQEntryTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.poNewRFQNum:int = obj["parameters"]
      pass

      """  output parameters  """  

class ECCUpdateFinal_input:
   """ Required : 
   ds
   reqType
   xmlDoc
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_RFQEntryTableset] = obj["ds"]
      self.reqType:str = obj["reqType"]
      self.xmlDoc:str = obj["xmlDoc"]
      pass

class ECCUpdateFinal_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_RFQEntryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class Erp_Tablesets_RFQEntryTableset:
   def __init__(self, obj):
      self.RFQHead:list[Erp_Tablesets_RFQHeadRow] = obj["RFQHead"]
      self.RFQHeadAttch:list[Erp_Tablesets_RFQHeadAttchRow] = obj["RFQHeadAttch"]
      self.RFQItem:list[Erp_Tablesets_RFQItemRow] = obj["RFQItem"]
      self.RFQItemAttch:list[Erp_Tablesets_RFQItemAttchRow] = obj["RFQItemAttch"]
      self.RFQPart:list[Erp_Tablesets_RFQPartRow] = obj["RFQPart"]
      self.RFQQty:list[Erp_Tablesets_RFQQtyRow] = obj["RFQQty"]
      self.RFQSourcing:list[Erp_Tablesets_RFQSourcingRow] = obj["RFQSourcing"]
      self.RFQVend:list[Erp_Tablesets_RFQVendRow] = obj["RFQVend"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_RFQHeadAttchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.RFQNum:int = obj["RFQNum"]
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

class Erp_Tablesets_RFQHeadListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.OpenRFQ:bool = obj["OpenRFQ"]
      """  Indicates if the RFQ is open or closed. This is set automatically when all the RFQItem records have been closed or can be set if the user voids the RFQ.  This field is not directly maintainable.  """  
      self.RFQNum:int = obj["RFQNum"]
      """  Number that uniquely identifies the RFQ document.  """  
      self.RFQDate:str = obj["RFQDate"]
      """  Date that this RFQ was entered.  """  
      self.RFQDueDate:str = obj["RFQDueDate"]
      """  The date the vendor responses are due.  """  
      self.BuyerID:str = obj["BuyerID"]
      """  The ID that links to the Purchasing Agent master file.  """  
      self.CommentText:str = obj["CommentText"]
      """  Contains comments about the RFQ. These will be printed on the RFQ document.  """  
      self.ReadyToPrint:bool = obj["ReadyToPrint"]
      """  Indicates if the RFQ is to selected for printing during the Mass Print process.  """  
      self.RespondDate:str = obj["RespondDate"]
      """  Date the supplier is to respond by  """  
      self.DecisionDate:str = obj["DecisionDate"]
      """  Date the PO is planned to be awarded  """  
      self.PostToWeb:bool = obj["PostToWeb"]
      """  Indicates the Supplier will respond via Suppliers workbench  """  
      self.PostDate:str = obj["PostDate"]
      """  Date Buyer posted the RFQ  """  
      self.GlbCompany:str = obj["GlbCompany"]
      """  Global Company identifier.  Used in Consolidated Purchasing.  """  
      self.GlbRFQNum:int = obj["GlbRFQNum"]
      """  Global RFQ identifier.  Used in Consolidated Purchasing.  """  
      self.AutoPrintReady:bool = obj["AutoPrintReady"]
      """  Field to use for the BAM to Auto-Print the Crystal Report or Bartender Labels associated to this table.  """  
      self.UOMClassID:str = obj["UOMClassID"]
      """  UOM Class ID  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.WebVendorExists:bool = obj["WebVendorExists"]
      self.BuyerIDName:str = obj["BuyerIDName"]
      """  Name of Purchasing Agent or Group. This is printed on the PO by the authorized signature line.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_RFQHeadListTableset:
   def __init__(self, obj):
      self.RFQHeadList:list[Erp_Tablesets_RFQHeadListRow] = obj["RFQHeadList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_RFQHeadRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.OpenRFQ:bool = obj["OpenRFQ"]
      """  Indicates if the RFQ is open or closed. This is set automatically when all the RFQItem records have been closed or can be set if the user voids the RFQ.  This field is not directly maintainable.  """  
      self.RFQNum:int = obj["RFQNum"]
      """  Number that uniquely identifies the RFQ document.  """  
      self.RFQDate:str = obj["RFQDate"]
      """  Date that this RFQ was entered.  """  
      self.RFQDueDate:str = obj["RFQDueDate"]
      """  The date the vendor responses are due.  """  
      self.BuyerID:str = obj["BuyerID"]
      """  The ID that links to the Purchasing Agent master file.  """  
      self.CommentText:str = obj["CommentText"]
      """  Contains comments about the RFQ. These will be printed on the RFQ document.  """  
      self.ReadyToPrint:bool = obj["ReadyToPrint"]
      """  Indicates if the RFQ is to selected for printing during the Mass Print process.  """  
      self.RespondDate:str = obj["RespondDate"]
      """  Date the supplier is to respond by  """  
      self.DecisionDate:str = obj["DecisionDate"]
      """  Date the PO is planned to be awarded  """  
      self.PostToWeb:bool = obj["PostToWeb"]
      """  Indicates the Supplier will respond via Suppliers workbench  """  
      self.PostDate:str = obj["PostDate"]
      """  Date Buyer posted the RFQ  """  
      self.GlbCompany:str = obj["GlbCompany"]
      """  Global Company identifier.  Used in Consolidated Purchasing.  """  
      self.GlbRFQNum:int = obj["GlbRFQNum"]
      """  Global RFQ identifier.  Used in Consolidated Purchasing.  """  
      self.AutoPrintReady:bool = obj["AutoPrintReady"]
      """  Field to use for the BAM to Auto-Print the Crystal Report or Bartender Labels associated to this table.  """  
      self.UOMClassID:str = obj["UOMClassID"]
      """  UOM Class ID  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.WebVendorExists:bool = obj["WebVendorExists"]
      self.BitFlag:int = obj["BitFlag"]
      self.BuyerIDName:str = obj["BuyerIDName"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_RFQItemAttchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.RFQNum:int = obj["RFQNum"]
      self.RFQLine:int = obj["RFQLine"]
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

class Erp_Tablesets_RFQItemRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.OpenItem:bool = obj["OpenItem"]
      """  Indicates if this line item is Open/Closed.  Set to "Closed" as when there are no longer any open RFQDtl records. This can also be closed when the user voids the RFQItem.  """  
      self.RFQNum:int = obj["RFQNum"]
      """  RFQ number  that the item is linked to.  """  
      self.RFQLine:int = obj["RFQLine"]
      """  The line number of this detail record on the RFQ. This number uniquely identifies the record within the RFQ. The number is not directly maintainable, it's assigned by the system when records are created.  """  
      self.LineDesc:str = obj["LineDesc"]
      """   Description of line item.
Defaults from JobOper, JobMtl or Part depending on the reference.  """  
      self.IUM:str = obj["IUM"]
      """  Issue (our) unit of measure.  """  
      self.PartNum:str = obj["PartNum"]
      """  OUR internal part number for this item.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  OUR revision number of the OUR part.  An optional field. Defaults from the most current  PartRev.RevisionNum.  """  
      self.CommentText:str = obj["CommentText"]
      """  Contains comments about the item. These will be printed on the RFQ. Defaults from the Job’s Material Purchasing comments.  """  
      self.ClassID:str = obj["ClassID"]
      """  The foreign key to the PartClass file.  May be blank, if entered must be valid in PartClass file.  Defaulted from Part.ClassID. The PartClass is used in determining a default G/L expense account.  """  
      self.JobNum:str = obj["JobNum"]
      """  Related job number.  """  
      self.QuoteNum:int = obj["QuoteNum"]
      """  Related Customer QuoteNum.  """  
      self.QuoteLine:int = obj["QuoteLine"]
      """  The QuoteLine that record is related to.  """  
      self.ItemType:str = obj["ItemType"]
      """  Mtl = Material, Sub = Subcontract  """  
      self.OpCode:str = obj["OpCode"]
      """   Operation Code - used to identify specific subcontracting operation that is needs to be quoted.
This field can be blank (raw materials) or must be valid in the OpMaster (subcontracts service).  """  
      self.AssemblySeq:int = obj["AssemblySeq"]
      """  Assembly sequence number that this rfq is associated with.  """  
      self.JobSeq:int = obj["JobSeq"]
      """  Job Seq of the requirement. Not maintainable.  """  
      self.RFQVendQuotes:int = obj["RFQVendQuotes"]
      """  The number of vendor quotes that are required for this rfq line.  """  
      self.GlbCompany:str = obj["GlbCompany"]
      """  Global Company identifier.  Used in Consolidated Purchasing.  """  
      self.GlbRFQNum:str = obj["GlbRFQNum"]
      """  Global RFQ identifier.  Used in Consolidated Purchasing.  """  
      self.GlbRFQLine:int = obj["GlbRFQLine"]
      """  Global RFQ Line identifier.  Used in Consolidated Purchasing.  """  
      self.RequiredQty:int = obj["RequiredQty"]
      """  Required Quantity from the source record (JobMtl/JobOper/QuoteMtl/QuoteOpr) used to create PORel.  Not user updatable.  """  
      self.RcvInspectionReq:bool = obj["RcvInspectionReq"]
      """  Indicates if inspection is required when items are received.  Used when create PODetail records  """  
      self.WarehouseCode:str = obj["WarehouseCode"]
      """  The warehouse that the material is allocated against.  """  
      self.SrcVendQuotes:int = obj["SrcVendQuotes"]
      """  Number of quotes required as indicated by the source file  """  
      self.ValidSrc:bool = obj["ValidSrc"]
      """  Indicates if the Source file (JobMtl,QuoteMtl,...) is a valid source record  """  
      self.PUM:str = obj["PUM"]
      """  The Purchase Unit of Measure  """  
      self.PurchasingFactor:int = obj["PurchasingFactor"]
      """  Used to capture the purchasing factor.  """  
      self.PurchasingFactorDirection:str = obj["PurchasingFactorDirection"]
      """  Indicates how Purchasing Factor is used in calculations.  If M (multiply), the Factor is multiplied, if  D (divide) the factor is divided.  """  
      self.ComplianceMsg:str = obj["ComplianceMsg"]
      """  Displays the cause why the item is not compliant.  """  
      self.UOMClassID:str = obj["UOMClassID"]
      """  UOM Class ID  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.ReqNum:int = obj["ReqNum"]
      """  Requisition number that the detail line is linked to.  """  
      self.ReqLine:int = obj["ReqLine"]
      """  The line number of detail record on the requisition.  This number uniquely identifies the record within the Requisition number.  The number is not directly maintainable; it's assigned by the system when records are created.  """  
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.NotCompliant:bool = obj["NotCompliant"]
      """  Indicates if the item on the line is not compliant on its source.  """  
      self.Source:str = obj["Source"]
      self.BitFlag:int = obj["BitFlag"]
      self.AssemblySeqDescription:str = obj["AssemblySeqDescription"]
      self.AttributeSetIDShortDescription:str = obj["AttributeSetIDShortDescription"]
      self.AttributeSetIDDescription:str = obj["AttributeSetIDDescription"]
      self.ClassDescription:str = obj["ClassDescription"]
      self.JobNumPartDescription:str = obj["JobNumPartDescription"]
      self.OpCodeOpDesc:str = obj["OpCodeOpDesc"]
      self.PartNumTrackInventoryAttributes:bool = obj["PartNumTrackInventoryAttributes"]
      self.PartNumAttrClassID:str = obj["PartNumAttrClassID"]
      self.PartNumTrackLots:bool = obj["PartNumTrackLots"]
      self.PartNumPartDescription:str = obj["PartNumPartDescription"]
      self.PartNumSellingFactor:int = obj["PartNumSellingFactor"]
      self.PartNumTrackDimension:bool = obj["PartNumTrackDimension"]
      self.PartNumIUM:str = obj["PartNumIUM"]
      self.PartNumPricePerCode:str = obj["PartNumPricePerCode"]
      self.PartNumSalesUM:str = obj["PartNumSalesUM"]
      self.PartNumTrackSerialNum:bool = obj["PartNumTrackSerialNum"]
      self.PartNumTrackInventoryByRevision:bool = obj["PartNumTrackInventoryByRevision"]
      self.QuoteLineLineDesc:str = obj["QuoteLineLineDesc"]
      self.QuoteNumCurrencyCode:str = obj["QuoteNumCurrencyCode"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_RFQPartRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.RFQNum:int = obj["RFQNum"]
      """  RFQNum  """  
      self.RFQLine:int = obj["RFQLine"]
      """  RFQLine  """  
      self.MfgNum:int = obj["MfgNum"]
      """  MfgNum  """  
      self.MfgPartNum:str = obj["MfgPartNum"]
      """  MfgPartNum  """  
      self.RFQInclude:bool = obj["RFQInclude"]
      """  True if this mfg part should be included on the RFQ, false if it should not be. Defaults to true.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.MfgNumName:str = obj["MfgNumName"]
      self.MfgNumID:str = obj["MfgNumID"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_RFQQtyRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.RFQNum:int = obj["RFQNum"]
      """  Number that uniquely identifies the RFQ document.  """  
      self.RFQLine:int = obj["RFQLine"]
      """  The line number of the detail record on the RFQ. This number uniquely identifies the record within the RFQ. The number not directly maintainable, it's assigned by the system when records are created.  """  
      self.QtyNum:int = obj["QtyNum"]
      """  An internally used integer assigned by the system to provide a unique key to the QuoteQty file. Allowing virtually unlimited quantities to be quoted for each detail line on a quote. This number is assigned as one greater than last one on file for the given QuoteDtl record.  """  
      self.Quantity:int = obj["Quantity"]
      """  The quantity for which the RFQ is requesting a quote.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.DspUOM:str = obj["DspUOM"]
      """  Display only field based on RFQItem.PUM  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RFQLineLineDesc:str = obj["RFQLineLineDesc"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_RFQSourcingRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.RFQNum:int = obj["RFQNum"]
      """  Number that uniquely identifies the RFQ document.  """  
      self.RFQLine:int = obj["RFQLine"]
      """  The line number of this detail record on the RFQ. This number uniquely identifies the record within the RFQ. The number is not directly maintainable, it's assigned by the system when records are created.  """  
      self.SourcingSeq:int = obj["SourcingSeq"]
      """  Sequence number used to complete the primary index and in case more than one records get created.  """  
      self.SourcingID:str = obj["SourcingID"]
      """  ID number that Sorcing retrieves in order to keep track of an auction.  """  
      self.SourcingStatus:str = obj["SourcingStatus"]
      """  Status of the Auction ( S = Send to Sourcing , P = Posted to Sourcing and Empty, Blank = Available to be sent)  """  
      self.AuctionTitle:str = obj["AuctionTitle"]
      """  Title of the auction  """  
      self.BidAnonimity:str = obj["BidAnonimity"]
      """  An option that restricts the information displayed about the winner of the event.  """  
      self.Category:str = obj["Category"]
      """  Category in which the items belong  """  
      self.Duration:int = obj["Duration"]
      """  The number of hours that the auction will stay online and open for bids  """  
      self.EventType:str = obj["EventType"]
      """  Type of Event Auction  """  
      self.ItemDescription:str = obj["ItemDescription"]
      """  Description of the item that is being sold / bought  """  
      self.MinOfferDec:int = obj["MinOfferDec"]
      """  Minimum Offer Decrement. The minimum amount of money that one user can bid over the current price.  """  
      self.PreviewDate:str = obj["PreviewDate"]
      """  Preview time is a given time for the users to preview the auction without being able to make bids yet.  """  
      self.PreviewTime:int = obj["PreviewTime"]
      """  Displays the time at which the auction can be previewed.  """  
      self.StartingDate:str = obj["StartingDate"]
      """  Start date is the date when the auction will be available for users to make bids.  """  
      self.StartingTime:int = obj["StartingTime"]
      """  Starting time for the users to be able to make bids.  """  
      self.ExpectedTotalPrice:int = obj["ExpectedTotalPrice"]
      """  Expected Total Price  """  
      self.ActualTotalPrice:int = obj["ActualTotalPrice"]
      """  Actual Total Price  """  
      self.AnonimityLevel:str = obj["AnonimityLevel"]
      """  Anonimity Level. Level of restriction for the information displayed about the winner of the event.  """  
      self.NegativeBids:bool = obj["NegativeBids"]
      """  Strictly speaking, negative bidding is simply placing a bid using a negative number.  """  
      self.UOMCode:str = obj["UOMCode"]
      """  Unit of Measure (used only on Dynamic Descent Events)  """  
      self.UnitQty:int = obj["UnitQty"]
      """  When creating a dynamic ascending or dynamic descending event you must enter the number of units you wish to buy or sell.  """  
      self.DecisionMakingRule:str = obj["DecisionMakingRule"]
      """  A rule that can determine how the winner of an event is selected.  """  
      self.StartingPrice:int = obj["StartingPrice"]
      """  The beginning or opening price of an item or service in a Dutch or reverse Dutch event.  """  
      self.MaxPrice:int = obj["MaxPrice"]
      """  The highest price a buyer will pay for an evented item.  """  
      self.PriceIncrement:int = obj["PriceIncrement"]
      """  Price Increment at each Interval. Used in buyer-centric events, it is the amount by which an event price increases per each interval of time.  """  
      self.TimeInterval:int = obj["TimeInterval"]
      """  Time Interval for each Price Increase  """  
      self.UNSPSC:str = obj["UNSPSC"]
      """  Universal Standard Products and Services Classification (UNSPSC)  """  
      self.FormsOfPayment:str = obj["FormsOfPayment"]
      """  Forms Of Payment  """  
      self.FreeOnBoard:str = obj["FreeOnBoard"]
      """  Designates who pays the carrier for the shipping of an item  """  
      self.Terms:str = obj["Terms"]
      """  The payment terms of a posting.  """  
      self.ShippingOptions:str = obj["ShippingOptions"]
      """  The various methods of shipping that apply to a posting.  """  
      self.Location:str = obj["Location"]
      """  The geographic location of an item for sale, or, in the case of an item for purchase, the geographic location where the item should be delivered.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.StartingTimeString:str = obj["StartingTimeString"]
      """  String representation of the StartingTime field  """  
      self.PreviewTimeString:str = obj["PreviewTimeString"]
      """  String representation of the Preview Time field  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_RFQVendRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.OpenItem:bool = obj["OpenItem"]
      """  Indicates if this line item is Open/Closed. Gets set to "Closed" when there are no longer any open RFQDtl records. This can also be closed when the user voids the RFQItem.  """  
      self.Response:str = obj["Response"]
      """   Indicates if the vendor has responded. This field is not directly maintainable, when price breaks are entered this is set to yes.
Valid values are 
 "W" = WAITING for response,
 "R" = response RECEIVED, and
 "N" = NO response RECEIVED, nor are we waiting for one.  """  
      self.RFQNum:int = obj["RFQNum"]
      """  RFQ number  that the item is linked to.  """  
      self.RFQLine:int = obj["RFQLine"]
      """  The line number of the detail record on the RFQ. This number uniquely identifies the record within the RFQ. The number is not directly maintainable, it's assigned by the system when records are created.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  Vendor's unique internal number.  """  
      self.PurPoint:str = obj["PurPoint"]
      """  Vendor Purchase Point ID.  """  
      self.ConNum:int = obj["ConNum"]
      """  Supplier contact linked to this RFQ  """  
      self.RespondVia:str = obj["RespondVia"]
      """  Can be "Web" or "Client"  """  
      self.RespondDate:str = obj["RespondDate"]
      """  Date Supplier responded to the RFQ.  Only used when the response came from the Web.  """  
      self.ComplianceMsg:str = obj["ComplianceMsg"]
      """  Compliance Message  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.VendorID:str = obj["VendorID"]
      self.VendorName:str = obj["VendorName"]
      self.OpenRFQ:bool = obj["OpenRFQ"]
      self.LineDescription:str = obj["LineDescription"]
      self.PartNum:str = obj["PartNum"]
      self.RevisionNum:str = obj["RevisionNum"]
      self.JobNum:str = obj["JobNum"]
      self.QuoteNum:int = obj["QuoteNum"]
      self.OpCode:str = obj["OpCode"]
      self.OpDescription:str = obj["OpDescription"]
      self.ResponseDescription:str = obj["ResponseDescription"]
      self.EffectiveDate:str = obj["EffectiveDate"]
      """  Vend Part Effective Date  """  
      self.RFQSource:str = obj["RFQSource"]
      """  Description of the Source field (either Job, Quote or blank)  """  
      self.RFQStatus:str = obj["RFQStatus"]
      self.BuyerID:str = obj["BuyerID"]
      """  Buyer Name  """  
      self.RFQDate:str = obj["RFQDate"]
      self.RFQDueDate:str = obj["RFQDueDate"]
      self.OurUOM:str = obj["OurUOM"]
      """  Our UOM  """  
      self.SupplierUOM:str = obj["SupplierUOM"]
      """  Supplier UOM  """  
      self.IUM:str = obj["IUM"]
      """  Base UOM Code from Part Master  """  
      self.PUM:str = obj["PUM"]
      """  The Purchasing Unit of measure for the Part.  """  
      self.CalcOurQty:int = obj["CalcOurQty"]
      self.CalcVendQty:int = obj["CalcVendQty"]
      self.NotCompliant:bool = obj["NotCompliant"]
      """  Indicates if the item on the line is not compliant on its source.  """  
      self.Selected:bool = obj["Selected"]
      self.AddressFormatted:str = obj["AddressFormatted"]
      """  Supplier Address  """  
      self.ResponseOptions:str = obj["ResponseOptions"]
      """  Valid Response options for combo.  """  
      self.AttributeDescription:str = obj["AttributeDescription"]
      self.AttributeSetID:int = obj["AttributeSetID"]
      self.AttributeShortDescription:str = obj["AttributeShortDescription"]
      self.BitFlag:int = obj["BitFlag"]
      self.RFQLineLineDesc:str = obj["RFQLineLineDesc"]
      self.VendorNumVendorID:str = obj["VendorNumVendorID"]
      self.VendorNumAddress2:str = obj["VendorNumAddress2"]
      self.VendorNumName:str = obj["VendorNumName"]
      self.VendorNumCountry:str = obj["VendorNumCountry"]
      self.VendorNumCity:str = obj["VendorNumCity"]
      self.VendorNumZIP:str = obj["VendorNumZIP"]
      self.VendorNumTermsCode:str = obj["VendorNumTermsCode"]
      self.VendorNumAddress3:str = obj["VendorNumAddress3"]
      self.VendorNumCurrencyCode:str = obj["VendorNumCurrencyCode"]
      self.VendorNumAddress1:str = obj["VendorNumAddress1"]
      self.VendorNumState:str = obj["VendorNumState"]
      self.VendorNumDefaultFOB:str = obj["VendorNumDefaultFOB"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_UpdExtRFQEntryTableset:
   def __init__(self, obj):
      self.RFQHead:list[Erp_Tablesets_RFQHeadRow] = obj["RFQHead"]
      self.RFQHeadAttch:list[Erp_Tablesets_RFQHeadAttchRow] = obj["RFQHeadAttch"]
      self.RFQItem:list[Erp_Tablesets_RFQItemRow] = obj["RFQItem"]
      self.RFQItemAttch:list[Erp_Tablesets_RFQItemAttchRow] = obj["RFQItemAttch"]
      self.RFQPart:list[Erp_Tablesets_RFQPartRow] = obj["RFQPart"]
      self.RFQQty:list[Erp_Tablesets_RFQQtyRow] = obj["RFQQty"]
      self.RFQSourcing:list[Erp_Tablesets_RFQSourcingRow] = obj["RFQSourcing"]
      self.RFQVend:list[Erp_Tablesets_RFQVendRow] = obj["RFQVend"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetByID_input:
   """ Required : 
   rfQNum
   """  
   def __init__(self, obj):
      self.rfQNum:int = obj["rfQNum"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_RFQEntryTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_RFQEntryTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_RFQEntryTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_RFQHeadListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewRFQHeadAttch_input:
   """ Required : 
   ds
   rfQNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_RFQEntryTableset] = obj["ds"]
      self.rfQNum:int = obj["rfQNum"]
      pass

class GetNewRFQHeadAttch_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_RFQEntryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewRFQHead_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_RFQEntryTableset] = obj["ds"]
      pass

class GetNewRFQHead_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_RFQEntryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewRFQItemAttch_input:
   """ Required : 
   ds
   rfQNum
   rfQLine
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_RFQEntryTableset] = obj["ds"]
      self.rfQNum:int = obj["rfQNum"]
      self.rfQLine:int = obj["rfQLine"]
      pass

class GetNewRFQItemAttch_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_RFQEntryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewRFQItem_input:
   """ Required : 
   ds
   rfQNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_RFQEntryTableset] = obj["ds"]
      self.rfQNum:int = obj["rfQNum"]
      pass

class GetNewRFQItem_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_RFQEntryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewRFQPart_input:
   """ Required : 
   ds
   rfQNum
   rfQLine
   mfgNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_RFQEntryTableset] = obj["ds"]
      self.rfQNum:int = obj["rfQNum"]
      self.rfQLine:int = obj["rfQLine"]
      self.mfgNum:int = obj["mfgNum"]
      pass

class GetNewRFQPart_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_RFQEntryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewRFQQty_input:
   """ Required : 
   ds
   rfQNum
   rfQLine
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_RFQEntryTableset] = obj["ds"]
      self.rfQNum:int = obj["rfQNum"]
      self.rfQLine:int = obj["rfQLine"]
      pass

class GetNewRFQQty_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_RFQEntryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewRFQSourcing_input:
   """ Required : 
   ds
   rfQNum
   rfQLine
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_RFQEntryTableset] = obj["ds"]
      self.rfQNum:int = obj["rfQNum"]
      self.rfQLine:int = obj["rfQLine"]
      pass

class GetNewRFQSourcing_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_RFQEntryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewRFQVend_input:
   """ Required : 
   ds
   rfQNum
   rfQLine
   vendorNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_RFQEntryTableset] = obj["ds"]
      self.rfQNum:int = obj["rfQNum"]
      self.rfQLine:int = obj["rfQLine"]
      self.vendorNum:int = obj["vendorNum"]
      pass

class GetNewRFQVend_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_RFQEntryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseRFQHead
   whereClauseRFQHeadAttch
   whereClauseRFQItem
   whereClauseRFQItemAttch
   whereClauseRFQPart
   whereClauseRFQQty
   whereClauseRFQSourcing
   whereClauseRFQVend
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseRFQHead:str = obj["whereClauseRFQHead"]
      self.whereClauseRFQHeadAttch:str = obj["whereClauseRFQHeadAttch"]
      self.whereClauseRFQItem:str = obj["whereClauseRFQItem"]
      self.whereClauseRFQItemAttch:str = obj["whereClauseRFQItemAttch"]
      self.whereClauseRFQPart:str = obj["whereClauseRFQPart"]
      self.whereClauseRFQQty:str = obj["whereClauseRFQQty"]
      self.whereClauseRFQSourcing:str = obj["whereClauseRFQSourcing"]
      self.whereClauseRFQVend:str = obj["whereClauseRFQVend"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_RFQEntryTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetSourcingStatus_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.oStatus:bool = obj["oStatus"]
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

class OnChangePartNum_input:
   """ Required : 
   newPart
   ds
   """  
   def __init__(self, obj):
      self.newPart:str = obj["newPart"]
      """  Proposed Part Number  """  
      self.ds:list[Erp_Tablesets_RFQEntryTableset] = obj["ds"]
      pass

class OnChangePartNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_RFQEntryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangePurPoint_input:
   """ Required : 
   ds
   pcVendorID
   pcVendorPP
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_RFQEntryTableset] = obj["ds"]
      self.pcVendorID:str = obj["pcVendorID"]
      """  VendorID  """  
      self.pcVendorPP:str = obj["pcVendorPP"]
      """  VendorPP  """  
      pass

class OnChangePurPoint_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_RFQEntryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeRFQItemPUM_input:
   """ Required : 
   ds
   ipPUM
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_RFQEntryTableset] = obj["ds"]
      self.ipPUM:str = obj["ipPUM"]
      """  PUM  """  
      pass

class OnChangeRFQItemPUM_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_RFQEntryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeVendorID_input:
   """ Required : 
   ds
   pcVendorID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_RFQEntryTableset] = obj["ds"]
      self.pcVendorID:str = obj["pcVendorID"]
      """  VendorID  """  
      pass

class OnChangeVendorID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_RFQEntryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeofBuyerID_input:
   """ Required : 
   piRFQNum
   newBuyerID
   ds
   """  
   def __init__(self, obj):
      self.piRFQNum:int = obj["piRFQNum"]
      """  RFQ Number  """  
      self.newBuyerID:str = obj["newBuyerID"]
      """  Buyer ID  """  
      self.ds:list[Erp_Tablesets_RFQEntryTableset] = obj["ds"]
      pass

class OnChangeofBuyerID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.rtnMessage:str = obj["parameters"]
      self.ds:list[Erp_Tablesets_RFQEntryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangingRevisionNum_input:
   """ Required : 
   revisionNum
   ds
   """  
   def __init__(self, obj):
      self.revisionNum:str = obj["revisionNum"]
      self.ds:list[Erp_Tablesets_RFQEntryTableset] = obj["ds"]
      pass

class OnChangingRevisionNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_RFQEntryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OpenRFQ_input:
   """ Required : 
   piRFQNum
   piOpenRFQ
   """  
   def __init__(self, obj):
      self.piRFQNum:int = obj["piRFQNum"]
      """  The RFQ number  """  
      self.piOpenRFQ:bool = obj["piOpenRFQ"]
      """  True/False open RFQ  """  
      pass

class OpenRFQ_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_RFQEntryTableset] = obj["returnObj"]
      pass

class ReOpenRFQLine_input:
   """ Required : 
   piRFQNum
   piRFQLine
   ds
   """  
   def __init__(self, obj):
      self.piRFQNum:int = obj["piRFQNum"]
      """  The RFQ number  """  
      self.piRFQLine:int = obj["piRFQLine"]
      """  The RFQ Line number  """  
      self.ds:list[Erp_Tablesets_RFQEntryTableset] = obj["ds"]
      pass

class ReOpenRFQLine_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_RFQEntryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtRFQEntryTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtRFQEntryTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_RFQEntryTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_RFQEntryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ValidateSelectedVendAttributes_input:
   """ Required : 
   inclVendAttrList
   exclVendAttrList
   """  
   def __init__(self, obj):
      self.inclVendAttrList:str = obj["inclVendAttrList"]
      """  Included Attributes  """  
      self.exclVendAttrList:str = obj["exclVendAttrList"]
      """  Excluded Attributes  """  
      pass

class ValidateSelectedVendAttributes_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      pass

class VendorWizard_input:
   """ Required : 
   piRFQNum
   piRFQLine
   plCheckPOs
   plCheckPriceBreaks
   plCheckRFQs
   pcIncludeVendAttrList
   pcExcludeVendAttrList
   pcComplianceList
   ds
   """  
   def __init__(self, obj):
      self.piRFQNum:int = obj["piRFQNum"]
      """  The RFQ number  """  
      self.piRFQLine:int = obj["piRFQLine"]
      """  The RFQ Line number  """  
      self.plCheckPOs:bool = obj["plCheckPOs"]
      """  The CheckPOs  """  
      self.plCheckPriceBreaks:bool = obj["plCheckPriceBreaks"]
      """  The CheckPriceBreaks  """  
      self.plCheckRFQs:bool = obj["plCheckRFQs"]
      """  The CheckRFQs  """  
      self.pcIncludeVendAttrList:str = obj["pcIncludeVendAttrList"]
      """  The include vendor attributes list  """  
      self.pcExcludeVendAttrList:str = obj["pcExcludeVendAttrList"]
      """  The exclude vendor attributes list  """  
      self.pcComplianceList:str = obj["pcComplianceList"]
      """  The Compliances the vendor must accomplish  """  
      self.ds:list[Erp_Tablesets_RFQEntryTableset] = obj["ds"]
      pass

class VendorWizard_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_RFQEntryTableset] = obj["ds"]
      self.pcMessage:str = obj["parameters"]
      pass

      """  output parameters  """  

