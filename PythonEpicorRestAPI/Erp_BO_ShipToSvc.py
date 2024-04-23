import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.ShipToSvc
# Description: Business Object for ShipTo.
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ShipToSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ShipToSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_ShipToes(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get ShipToes items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ShipToes
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ShipToRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ShipToSvc/ShipToes",headers=creds) as resp:
           return await resp.json()

async def post_ShipToes(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ShipToes
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ShipToRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.ShipToRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ShipToSvc/ShipToes", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_ShipToes_Company_CustNum_ShipToNum(Company, CustNum, ShipToNum, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ShipTo item
   Description: Calls GetByID to retrieve the ShipTo item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ShipTo
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param CustNum: Desc: CustNum   Required: True
      :param ShipToNum: Desc: ShipToNum   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ShipToRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ShipToSvc/ShipToes(" + Company + "," + CustNum + "," + ShipToNum + ")",headers=creds) as resp:
           return await resp.json()

async def patch_ShipToes_Company_CustNum_ShipToNum(Company, CustNum, ShipToNum, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update ShipTo for the service
   Description: Calls UpdateExt to update ShipTo. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ShipTo
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param CustNum: Desc: CustNum   Required: True
      :param ShipToNum: Desc: ShipToNum   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.ShipToRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.ShipToSvc/ShipToes(" + Company + "," + CustNum + "," + ShipToNum + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_ShipToes_Company_CustNum_ShipToNum(Company, CustNum, ShipToNum, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete ShipTo item
   Description: Call UpdateExt to delete ShipTo item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ShipTo
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param CustNum: Desc: CustNum   Required: True
      :param ShipToNum: Desc: ShipToNum   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.ShipToSvc/ShipToes(" + Company + "," + CustNum + "," + ShipToNum + ")",headers=creds) as resp:
           return await resp.json()

async def get_ShipToes_Company_CustNum_ShipToNum_ShipToLabExpRates(Company, CustNum, ShipToNum, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get ShipToLabExpRates items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_ShipToLabExpRates1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param CustNum: Desc: CustNum   Required: True
      :param ShipToNum: Desc: ShipToNum   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ShipToLabExpRateRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ShipToSvc/ShipToes(" + Company + "," + CustNum + "," + ShipToNum + ")/ShipToLabExpRates",headers=creds) as resp:
           return await resp.json()

async def get_ShipToes_Company_CustNum_ShipToNum_ShipToLabExpRates_Company_CustNum_ShipToNum_ExpenseCode(Company, CustNum, ShipToNum, ExpenseCode, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ShipToLabExpRate item
   Description: Calls GetByID to retrieve the ShipToLabExpRate item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ShipToLabExpRate1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param CustNum: Desc: CustNum   Required: True
      :param ShipToNum: Desc: ShipToNum   Required: True   Allow empty value : True
      :param ExpenseCode: Desc: ExpenseCode   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ShipToLabExpRateRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ShipToSvc/ShipToes(" + Company + "," + CustNum + "," + ShipToNum + ")/ShipToLabExpRates(" + Company + "," + CustNum + "," + ShipToNum + "," + ExpenseCode + ")",headers=creds) as resp:
           return await resp.json()

async def get_ShipToes_Company_CustNum_ShipToNum_ShipToAttches(Company, CustNum, ShipToNum, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get ShipToAttches items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_ShipToAttches1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param CustNum: Desc: CustNum   Required: True
      :param ShipToNum: Desc: ShipToNum   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ShipToAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ShipToSvc/ShipToes(" + Company + "," + CustNum + "," + ShipToNum + ")/ShipToAttches",headers=creds) as resp:
           return await resp.json()

async def get_ShipToes_Company_CustNum_ShipToNum_ShipToAttches_Company_CustNum_ShipToNum_DrawingSeq(Company, CustNum, ShipToNum, DrawingSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ShipToAttch item
   Description: Calls GetByID to retrieve the ShipToAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ShipToAttch1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param CustNum: Desc: CustNum   Required: True
      :param ShipToNum: Desc: ShipToNum   Required: True   Allow empty value : True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ShipToAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ShipToSvc/ShipToes(" + Company + "," + CustNum + "," + ShipToNum + ")/ShipToAttches(" + Company + "," + CustNum + "," + ShipToNum + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_ShipToLabExpRates(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get ShipToLabExpRates items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ShipToLabExpRates
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ShipToLabExpRateRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ShipToSvc/ShipToLabExpRates",headers=creds) as resp:
           return await resp.json()

async def post_ShipToLabExpRates(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ShipToLabExpRates
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ShipToLabExpRateRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.ShipToLabExpRateRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ShipToSvc/ShipToLabExpRates", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_ShipToLabExpRates_Company_CustNum_ShipToNum_ExpenseCode(Company, CustNum, ShipToNum, ExpenseCode, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ShipToLabExpRate item
   Description: Calls GetByID to retrieve the ShipToLabExpRate item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ShipToLabExpRate
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param CustNum: Desc: CustNum   Required: True
      :param ShipToNum: Desc: ShipToNum   Required: True   Allow empty value : True
      :param ExpenseCode: Desc: ExpenseCode   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ShipToLabExpRateRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ShipToSvc/ShipToLabExpRates(" + Company + "," + CustNum + "," + ShipToNum + "," + ExpenseCode + ")",headers=creds) as resp:
           return await resp.json()

async def patch_ShipToLabExpRates_Company_CustNum_ShipToNum_ExpenseCode(Company, CustNum, ShipToNum, ExpenseCode, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update ShipToLabExpRate for the service
   Description: Calls UpdateExt to update ShipToLabExpRate. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ShipToLabExpRate
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param CustNum: Desc: CustNum   Required: True
      :param ShipToNum: Desc: ShipToNum   Required: True   Allow empty value : True
      :param ExpenseCode: Desc: ExpenseCode   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.ShipToLabExpRateRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.ShipToSvc/ShipToLabExpRates(" + Company + "," + CustNum + "," + ShipToNum + "," + ExpenseCode + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_ShipToLabExpRates_Company_CustNum_ShipToNum_ExpenseCode(Company, CustNum, ShipToNum, ExpenseCode, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete ShipToLabExpRate item
   Description: Call UpdateExt to delete ShipToLabExpRate item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ShipToLabExpRate
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param CustNum: Desc: CustNum   Required: True
      :param ShipToNum: Desc: ShipToNum   Required: True   Allow empty value : True
      :param ExpenseCode: Desc: ExpenseCode   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.ShipToSvc/ShipToLabExpRates(" + Company + "," + CustNum + "," + ShipToNum + "," + ExpenseCode + ")",headers=creds) as resp:
           return await resp.json()

async def get_ShipToAttches(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get ShipToAttches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ShipToAttches
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ShipToAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ShipToSvc/ShipToAttches",headers=creds) as resp:
           return await resp.json()

async def post_ShipToAttches(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ShipToAttches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ShipToAttchRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.ShipToAttchRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ShipToSvc/ShipToAttches", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_ShipToAttches_Company_CustNum_ShipToNum_DrawingSeq(Company, CustNum, ShipToNum, DrawingSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ShipToAttch item
   Description: Calls GetByID to retrieve the ShipToAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ShipToAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param CustNum: Desc: CustNum   Required: True
      :param ShipToNum: Desc: ShipToNum   Required: True   Allow empty value : True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ShipToAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ShipToSvc/ShipToAttches(" + Company + "," + CustNum + "," + ShipToNum + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_ShipToAttches_Company_CustNum_ShipToNum_DrawingSeq(Company, CustNum, ShipToNum, DrawingSeq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update ShipToAttch for the service
   Description: Calls UpdateExt to update ShipToAttch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ShipToAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param CustNum: Desc: CustNum   Required: True
      :param ShipToNum: Desc: ShipToNum   Required: True   Allow empty value : True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.ShipToAttchRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.ShipToSvc/ShipToAttches(" + Company + "," + CustNum + "," + ShipToNum + "," + DrawingSeq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_ShipToAttches_Company_CustNum_ShipToNum_DrawingSeq(Company, CustNum, ShipToNum, DrawingSeq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete ShipToAttch item
   Description: Call UpdateExt to delete ShipToAttch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ShipToAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param CustNum: Desc: CustNum   Required: True
      :param ShipToNum: Desc: ShipToNum   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.ShipToSvc/ShipToAttches(" + Company + "," + CustNum + "," + ShipToNum + "," + DrawingSeq + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ShipToListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ShipToSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseShipTo, whereClauseShipToAttch, whereClauseShipToLabExpRate, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClauseShipTo=" + whereClauseShipTo
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseShipToAttch=" + whereClauseShipToAttch
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseShipToLabExpRate=" + whereClauseShipToLabExpRate
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ShipToSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(custNum, shipToNum, epicorHeaders = None):
   """  
   Summary: Invoke method GetByID
   Description: Returns a DataSet given the primary key.
   OperationID: Get_GetByID
   Required: True
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
   params += "custNum=" + custNum
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "shipToNum=" + shipToNum

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ShipToSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_GetListFilterCustomer(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetListFilterCustomer
   Description: Filter ShipTo by Customer.  Call normal GetList method.
   OperationID: GetListFilterCustomer
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetListFilterCustomer_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetListFilterCustomer_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ShipToSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewShipTo(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewShipTo
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewShipTo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewShipTo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewShipTo_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ShipToSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewShipToAttch(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewShipToAttch
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewShipToAttch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewShipToAttch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewShipToAttch_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ShipToSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewShipToLabExpRate(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewShipToLabExpRate
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewShipToLabExpRate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewShipToLabExpRate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewShipToLabExpRate_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ShipToSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ShipToSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ShipToSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ShipToSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ShipToSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ShipToSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ShipToSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ShipToAttchRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_ShipToAttchRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ShipToLabExpRateRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_ShipToLabExpRateRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ShipToListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_ShipToListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ShipToRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_ShipToRow] = obj["value"]
      pass

class Erp_Tablesets_ShipToAttchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.CustNum:int = obj["CustNum"]
      self.ShipToNum:str = obj["ShipToNum"]
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

class Erp_Tablesets_ShipToLabExpRateRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.CustNum:int = obj["CustNum"]
      """  CustNum  """  
      self.ShipToNum:str = obj["ShipToNum"]
      """  ShipToNum  """  
      self.ExpenseCode:str = obj["ExpenseCode"]
      """  ExpenseCode  """  
      self.RateType:int = obj["RateType"]
      """  RateType  """  
      self.RateMultiplier:int = obj["RateMultiplier"]
      """  RateMultiplier  """  
      self.FixedRate:int = obj["FixedRate"]
      """  FixedRate  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.BitFlag:int = obj["BitFlag"]
      self.ShipToShipToNum:str = obj["ShipToShipToNum"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ShipToListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.CustNum:int = obj["CustNum"]
      """  The Customer.CustNum value of the customer that the record is related to.  """  
      self.ShipToNum:str = obj["ShipToNum"]
      """  The ID assigned by the user which makes this record unique for the customer.  When a customer is created a ShipTo record is automatically created by the system for that customer with a ShipToNum equal to NULL.  """  
      self.Name:str = obj["Name"]
      """  Name of the ShipTo. When creating new records the Customer.Name is used as a default.  """  
      self.Address1:str = obj["Address1"]
      """  The first line of the ShipTo address.  """  
      self.Address2:str = obj["Address2"]
      """  The second line of the ShipTo address.  """  
      self.Address3:str = obj["Address3"]
      """  The third line of the ShipTo address.  """  
      self.City:str = obj["City"]
      """  The city portion of the ShipTo address.  """  
      self.State:str = obj["State"]
      """  The state or province portion of the ShipTo address.  """  
      self.ZIP:str = obj["ZIP"]
      """  The zip or postal code portion of the ShipTo address.  """  
      self.Country:str = obj["Country"]
      """  The country portion of the ShipTo address.  """  
      self.ResaleID:str = obj["ResaleID"]
      """  The State Tax Identification Number. Used in Order Entry and prints on Sales Acknowledgements.  """  
      self.SalesRepCode:str = obj["SalesRepCode"]
      """  The SalesRep.SalesRepCode value of the default salesperson for the customer. Used as a default in Order Entry and Invoice entry. The SalesRep from the customer master is used as an initial default when creating new ship to.  """  
      self.TerritoryID:str = obj["TerritoryID"]
      """  The SalesTer.TerritoryID value of the territory the customer is assigned to.  """  
      self.ShipViaCode:str = obj["ShipViaCode"]
      """  The ShipVia.ShipViaCode value of the default ShipVia assigned to the customer. Used as a default in Order Entry, Shipping and Invoicing.  The shipvia from the customer record for this shipto is used as the initial default when creating new ShipTo records.  """  
      self.PrimSCon:int = obj["PrimSCon"]
      """  The CustCnt.ConNum of the default shipping contact for the ShipTo location. The primary shipping contact is used as a default in the shipping process.  """  
      self.FaxNum:str = obj["FaxNum"]
      """  The fax number for the ShipTo location. isplayed in Order entry when no shipping contact is given for or when contact has a blank phone number.  """  
      self.PhoneNum:str = obj["PhoneNum"]
      """  The business phone number for the ShipTo location. Displayed in Order entry when no shipping contact is given for or when contact has a blank phone number.  """  
      self.TaxExempt:str = obj["TaxExempt"]
      """  Determines whether or not the ShipTo location is normally exempt from sales tax. Used as a default in invoice entry.  If the field is non-blank it is considered exempt.   This code is totally user definable and no validation is required.  """  
      self.EDIShipNum:str = obj["EDIShipNum"]
      """  A mutually agreed upon value that links a customer's EDI shipto record (an N1 / ST) to the Manufacturing System DB ShipTo record.  """  
      self.CountryNum:int = obj["CountryNum"]
      """  The Country.CountryNum value of the country selected in the ShipTo.Country field.  """  
      self.LangNameID:str = obj["LangNameID"]
      """  The LangName.LangNameID value of the default Language assigned to the ShipTo location. This controls which language will be selected when extracting part descriptions from PartLangDesc table.  """  
      self.BorderCrossing:str = obj["BorderCrossing"]
      """  Area/city code from where goods cross the border. This field is intended for Intrastat reporting. The field can be blank to indicate the value from the Customer table. This field is only visible if ISSyst.EnableHarbour is set.  """  
      self.FormatStr:str = obj["FormatStr"]
      """  Optional custom address format for the ShipTo location.  """  
      self.TaxRegionCode:str = obj["TaxRegionCode"]
      """  Contains the TaxRgn.TaxRegionCode value of the customer's tax region for purposes of Sales Tax calculations.  """  
      self.EMailAddress:str = obj["EMailAddress"]
      """  The email address of the ShipTo location.  """  
      self.TerritorySelect:str = obj["TerritorySelect"]
      """   Determines how the ShipTo location should be assigned to a territory. There are 3 methods for Territory assignment in Ship-to:

Sync - Keep the ShipTo territory synchronized with the territory on the
       main customer record. (ShipTo.TerritoryID = Customer.TerritoryID)
Syst - Let the system (Get Territory) determine the territory to assign         to the ShipTo based on territory boundaries.
Lock - Check this method after assigning the territory manually to 
       prevent the system from attempting to reassign the territory.  """  
      self.PendingTerritoryID:str = obj["PendingTerritoryID"]
      """  The pending sales territory that the customer will be assigned to based on changes to the territory boundaries.  This functionality is only available with the CRM module.  """  
      self.CreatedByEDI:bool = obj["CreatedByEDI"]
      """  Determines whether or not the ShipTo record was created by an EDI transaction.  """  
      self.ExternalID:str = obj["ExternalID"]
      """  Unique identifier of the ShipTo from an external General Ledger interface such as the EuroFinancial integration.  """  
      self.TaxAuthorityCode:str = obj["TaxAuthorityCode"]
      """  The TaxAuthorityCd.TaxAuthorityCode value of the Tax Authority assigned to this ShipTo location.  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Disable this record from receiving global updates.  """  
      self.EDICode:str = obj["EDICode"]
      """  The Trading Partner ID that is used for incoming and outgoing EDI transactions.  """  
      self.DemandDeliveryDays:int = obj["DemandDeliveryDays"]
      """  Days to use in calculating the Order Detail Ship By date from the incoming need by date.  """  
      self.DemandDateType:str = obj["DemandDateType"]
      """   Indicates incoming date type.  Values are:
S - Shipping Date
N - Need By Date  """  
      self.DemandAddLeadTime:int = obj["DemandAddLeadTime"]
      """  The number of days from today to give a warning when adding a new order release record from an incoming shipping schedule.  """  
      self.DemandAddAction:str = obj["DemandAddAction"]
      """  Indicates what type of action to take if the add lead time is breeched.  Options are B (reject the change) or W (warning - alert that the lead time has been breeched but allow the record to be accepted).  """  
      self.DemandChangeLeadTime:int = obj["DemandChangeLeadTime"]
      """  The number of days from today to give a warning when changing an order release record from an incoming shipping schedule.  This does not include changes to quantity or dates.  """  
      self.DemandChangeAction:str = obj["DemandChangeAction"]
      """  Indicates what type of action to take if the change lead time is breeched.  Options are B (reject the change) or W (warning - alert that the lead time has been breeched but allow the record to be accepted).  """  
      self.DemandCancelLeadTime:int = obj["DemandCancelLeadTime"]
      """  The number of days from today to give a warning when canceling an order release record from an incoming shipping schedule.  """  
      self.DemandCancelAction:str = obj["DemandCancelAction"]
      """  Indicates what type of action to take if the cancel lead time is breeched.  Options are B (reject the change) or W (warning - alert that the lead time has been breeched but allow the record to be accepted).  """  
      self.DemandNewLineLeadTime:int = obj["DemandNewLineLeadTime"]
      """  The number of days from today to give a warning when adding a new order line record from an incoming shipping schedule.  """  
      self.DemandNewLineAction:str = obj["DemandNewLineAction"]
      """  Indicates what type of action to take if the new line lead time is breeched.  Options are B (reject the change) or W (warning - alert that the lead time has been breeched but allow the record to be accepted).  """  
      self.DemandQtyChangeLeadTime:int = obj["DemandQtyChangeLeadTime"]
      """  The number of days from today to give a warning when changing the quantity on an order release record from an incoming shipping schedule.  """  
      self.DemandQtyChangeAction:str = obj["DemandQtyChangeAction"]
      """  Indicates what type of action to take if the quantity change lead time is breeched.  Options are B (reject the change) or W (warning - alert that the lead time has been breeched but allow the record to be accepted).  """  
      self.DemandChangeDateLeadTime:int = obj["DemandChangeDateLeadTime"]
      """  The number of days from today to give a warning when changing the date on an order release record from an incoming shipping schedule.  """  
      self.DemandChangeDateAction:str = obj["DemandChangeDateAction"]
      """  Indicates what type of action to take if the change date lead time is breeched.  Options are B (reject the change) or W (warning - alert that the lead time has been breeched but allow the record to be accepted).  """  
      self.TradingPartnerName:str = obj["TradingPartnerName"]
      """  The trading partner name.  """  
      self.ResDelivery:bool = obj["ResDelivery"]
      """  Is this a residential delivery  """  
      self.SatDelivery:bool = obj["SatDelivery"]
      """  Is a Saturday delivery acceptable  """  
      self.SatPickup:bool = obj["SatPickup"]
      """  Is a Saturday pickup available  """  
      self.Hazmat:bool = obj["Hazmat"]
      """  Hazmat or Dangerous Goods delivery  """  
      self.DocOnly:bool = obj["DocOnly"]
      """  Documents Only delivery  """  
      self.RefNotes:str = obj["RefNotes"]
      """  Reference Notes for the delivery  """  
      self.ApplyChrg:bool = obj["ApplyChrg"]
      """  Apply Handling Charge to shipment  """  
      self.ChrgAmount:int = obj["ChrgAmount"]
      """  Handling Charge Amount  """  
      self.COD:bool = obj["COD"]
      """  Prefer COD delivery  """  
      self.CODFreight:bool = obj["CODFreight"]
      """  Add Freight COD Amount owed  """  
      self.CODCheck:bool = obj["CODCheck"]
      """  Cashier's Check or Money order is required on COD Delivery  """  
      self.CODAmount:int = obj["CODAmount"]
      """  Amount due on Cashier's check or money order  """  
      self.GroundType:str = obj["GroundType"]
      """  Valid Values are blank, "Any" (Any Payment), "GF" (Guaranteed Funds), or "Cash" (Currency)  """  
      self.NotifyFlag:bool = obj["NotifyFlag"]
      """  Indicates whether to send an email notification of delivery  """  
      self.NotifyEMail:str = obj["NotifyEMail"]
      """  The list of email address to notify about a delivery  """  
      self.DeclaredIns:bool = obj["DeclaredIns"]
      """  Flag to indicate that an insurance value was declared on delivery  """  
      self.DeclaredAmt:int = obj["DeclaredAmt"]
      """  Declared Insurance Amount  """  
      self.PeriodicityCode:int = obj["PeriodicityCode"]
      """  Periodicity Code.  Must be a valid code in the Periodicity table.  """  
      self.ServSignature:bool = obj["ServSignature"]
      """  Service delivery requires signature  """  
      self.ServAlert:bool = obj["ServAlert"]
      """  Service Priority Alert flag  """  
      self.ServHomeDel:bool = obj["ServHomeDel"]
      """  Service Home Delivery allowed  """  
      self.DeliveryType:str = obj["DeliveryType"]
      """  Service Home Delivery Type Code  """  
      self.ServDeliveryDate:str = obj["ServDeliveryDate"]
      """  Service Home Delivery date  """  
      self.ServPhone:str = obj["ServPhone"]
      """  Home delivery phone number  """  
      self.ServInstruct:str = obj["ServInstruct"]
      """  Service Delivery Instructions  """  
      self.ServRelease:bool = obj["ServRelease"]
      """  Service Signature release is on file  """  
      self.ServAuthNum:str = obj["ServAuthNum"]
      """  Service Signature Release authorization number  """  
      self.ServRef1:str = obj["ServRef1"]
      """  Service Reference 1  """  
      self.CommercialInvoice:bool = obj["CommercialInvoice"]
      """  Added for international shipping, Is a commercial invoice required  """  
      self.ServRef2:str = obj["ServRef2"]
      """  Service Reference 2  """  
      self.ShipExprtDeclartn:bool = obj["ShipExprtDeclartn"]
      """  Added for international shipping. Shipper's Export Declaration required  """  
      self.ServRef3:str = obj["ServRef3"]
      """  Service Reference 3  """  
      self.CertOfOrigin:bool = obj["CertOfOrigin"]
      """  For International shipping.  Certificate of Orgin required.  """  
      self.ServRef4:str = obj["ServRef4"]
      """  Service Reference 4  """  
      self.LetterOfInstr:bool = obj["LetterOfInstr"]
      """  For International shipping.  Shipper's Letter of Instruction.  """  
      self.ServRef5:str = obj["ServRef5"]
      """  Service Reference 5  """  
      self.HazardousShipment:bool = obj["HazardousShipment"]
      """  International Shipping - HazardousShipment  """  
      self.OverrideCarrier:bool = obj["OverrideCarrier"]
      """  Override Carrier Defaults.  If not checked then the customer values will be used if overriden else the Site values  """  
      self.IntrntlShip:bool = obj["IntrntlShip"]
      """  Is this an International shipment  """  
      self.OverrideService:bool = obj["OverrideService"]
      """  Override Service Options.  If not checked then the customer values will be used if overriden else the Site values  """  
      self.DemandUseCustomerValues:bool = obj["DemandUseCustomerValues"]
      """  Indicates if the demand fields from the customer should be used.  """  
      self.TaxRegReason:str = obj["TaxRegReason"]
      """  Tax Payer Registration Reason Code  """  
      self.EarlyBuffer:int = obj["EarlyBuffer"]
      """  Used to calculate on-time delivery performance rating  """  
      self.OrgRegCode:str = obj["OrgRegCode"]
      """  Organization Registration Code  """  
      self.LateBuffer:int = obj["LateBuffer"]
      """  Used to calculate on-time delivery performance rating  """  
      self.DemandUnitPriceDiff:bool = obj["DemandUnitPriceDiff"]
      """  Indicates if the unit price between the demand and the contract should be validated.  If this flag is checked, and the prices are different, when the demand is accepted a record will be written to the DemandLog table.  """  
      self.DemandUnitPriceDiffAction:str = obj["DemandUnitPriceDiffAction"]
      """  Indicates what type of action to take if the unit price between the demand and the contract is different.  Options are B (reject the change) or W (warning - alert that the unit price is different but allow the record to be accepted).  """  
      self.ExcFromVal:bool = obj["ExcFromVal"]
      """  A flag that indicates whether this address should be validated by the tax service.  """  
      self.AddressVal:bool = obj["AddressVal"]
      """  A flag indicating that an address has already been validated. This helps improve the performance of the bulk address validation process by allowing address that have already been validated to be skipped. This flag is set anytime a successful validation is performed, either by the bulk address validation or validation from the Customer form.  """  
      self.DemandCheckForPart:bool = obj["DemandCheckForPart"]
      """  Check for the part in the Part master.  """  
      self.DemandCheckForPartAction:str = obj["DemandCheckForPartAction"]
      """  Indicates what type of action to take if the Check for Part options is selected and the part is not in the part master file.  Options are B (reject the change) or W (warning - alert that the part is not in the part master but allow the record to be accepted).  """  
      self.FFID:str = obj["FFID"]
      """  International Shipping. Frieght Forwarder ID  """  
      self.FFAddress1:str = obj["FFAddress1"]
      """  International Shipping. The first line of the Frieght Forwarder main address.  """  
      self.FFAddress2:str = obj["FFAddress2"]
      """  International Shipping. The second line of the Frieght Forwarder main address.  """  
      self.FFCity:str = obj["FFCity"]
      """  Shipping, The city portion of the Frieght Forwarder main address.  """  
      self.FFState:str = obj["FFState"]
      """  International Shipping. The state or province portion of the shipment Frieght Forwarder main address.  """  
      self.FFZip:str = obj["FFZip"]
      """  International Shipping. The zip or postal code portion of the shipping Frieght Forwarder main address.  """  
      self.FFCountry:str = obj["FFCountry"]
      """  International shipping. The country of the Frieght Forwarder .  """  
      self.FFContact:str = obj["FFContact"]
      """  International Shipping. Frieght Forwarder Contact  """  
      self.FFCompName:str = obj["FFCompName"]
      """  International Shipping. Frieght Forwarder company name  """  
      self.FFPhoneNum:str = obj["FFPhoneNum"]
      """  International Shipping. Frieght Forwarder Phone number  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  Userid of user who made the last change to this record.  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  The date that the record was last changed  """  
      self.ChangeTime:int = obj["ChangeTime"]
      """  The time that the record was last change (seconds since midnight)  """  
      self.IndividualPackIDs:bool = obj["IndividualPackIDs"]
      """  Individual Pack IDs  """  
      self.FFCountryNum:int = obj["FFCountryNum"]
      """  Freight Forwarder Third address line  """  
      self.NonStdPkg:bool = obj["NonStdPkg"]
      """  Additional Handling flag  """  
      self.DeliveryConf:int = obj["DeliveryConf"]
      """   Determines the level of delivery confirmation.
1 - No Signature Required
2 - Adult Signature Required
3 - Confirmation Required
4 - Verbal Confirmation Required  """  
      self.AddlHdlgFlag:bool = obj["AddlHdlgFlag"]
      """  Non Standard Packaging  """  
      self.UPSQuantumView:bool = obj["UPSQuantumView"]
      """  UPS Quantum View  """  
      self.UPSQVShipFromName:str = obj["UPSQVShipFromName"]
      """  UPS Quantum View From Name  """  
      self.UPSQVMemo:str = obj["UPSQVMemo"]
      """  UPS Quantum View Memo  """  
      self.FFAddress3:str = obj["FFAddress3"]
      """  Freight Forwarder Country portion of the address  """  
      self.ETCAddrChg:bool = obj["ETCAddrChg"]
      """  Used to determine if an address changed because of the tax integration.  If true, the tax integration changed the address.  """  
      self.IsAlternate:bool = obj["IsAlternate"]
      """  Indicates if this is a alternate ShipTo. An alternate is a Shipto that is valid for this customer, but is defined/maintained by the "master" customer. See ShipTo.MasterCustNum/MasterShiptoNum.  """  
      self.MasterCustNum:int = obj["MasterCustNum"]
      """  Pertains to Alternate Shipto (IsAlternate). Contains the CustNum of the Shipto record that is the "Master". Changes made to the Master, are replicated to the alternates.  """  
      self.MasterShipToNum:str = obj["MasterShipToNum"]
      """  Pertains to Alternate Shipto (IsAlternate). Contains the ShipToNum of the Shipto record that is the "Master". Changes made to the Master, are replicated to the alternates.  """  
      self.DemandCheckForRev:bool = obj["DemandCheckForRev"]
      """  Check for Revision  """  
      self.DemandCheckForRevAction:str = obj["DemandCheckForRevAction"]
      """  Check for Revision Action  """  
      self.DemandCheckPartialShip:bool = obj["DemandCheckPartialShip"]
      """  Flag for checking partial Shipment for Demand Entry.  """  
      self.DemandCheckShipAction:str = obj["DemandCheckShipAction"]
      """  Check Partial Shipments Action: B =Stop  and W = Warning  """  
      self.DemandCloseRejSkd:bool = obj["DemandCloseRejSkd"]
      """  Define if at the moment of processing a demand the process should also close those rejected schedules that remain at demand entry  """  
      self.DemandPricing:str = obj["DemandPricing"]
      """  Defines if Internal Pricing or Customer Pricing will be used for checking price differences  """  
      self.PriceTolerance:int = obj["PriceTolerance"]
      """  Defines the tolerance for price difference validations  """  
      self.CheckDateCapPromise:bool = obj["CheckDateCapPromise"]
      """  If this flags is turned on then Demand CTP will automatically be executed as a part of the demand to order process.  """  
      self.CheckConfirmCapPromise:bool = obj["CheckConfirmCapPromise"]
      """  Confirm or not the Capable to Promise jobs from Demand Entry  """  
      self.CheckUpdateCapPromise:bool = obj["CheckUpdateCapPromise"]
      """  If checked, Updates the date in Demand Entry  """  
      self.DemandCapPromiseDate:str = obj["DemandCapPromiseDate"]
      """  This field will define the dates that will be validated as a part of the demand to order process. The valid values for this combo will be:  Need By (N), Ship By (S) and Both (B)  """  
      self.DemandCapPromiseAction:str = obj["DemandCapPromiseAction"]
      """  The value on this field will define the action to be taken when validating CTP. The valid values for this combo box will be: Warning (W) and Stop (S)  """  
      self.DemandCapPromiseUpdate:str = obj["DemandCapPromiseUpdate"]
      """   This field will define the dates that will be updated as a part of the demand to order process. The valid options will be:
Need By (N), Ship By (S) and Both  (B) NOTE .-In all the cases above the update of date will only be done if the CTP dates are beyond the dates on the file.  """  
      self.OTSmartString:bool = obj["OTSmartString"]
      """  When set to TRUE the smart string functionality will only be processed when the incoming demand is new. After it has been processed and saved, if a retransmission is sent the smart string values will be ignored.  """  
      self.LegalName:str = obj["LegalName"]
      """  Full Legal name  """  
      self.DemandCheckConfig:bool = obj["DemandCheckConfig"]
      """  If true then demand will be rejected when one or more demand lines are not configured properly. Applies only to Configurable parts.  """  
      self.DemandCheckCfgAction:str = obj["DemandCheckCfgAction"]
      """  Indicates the action to be taken if configuration values have not been entered for one or more demand lines.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.AddrList:str = obj["AddrList"]
      """  Address in formatted delimited list  """  
      self.ContactName:str = obj["ContactName"]
      """  Used for ContactTracker.  This is needed so the UI can relate the Contact Tracker tables together.  """  
      self.DspFormatStr:str = obj["DspFormatStr"]
      """  Display Format String  """  
      self.TerrSelectFlag:str = obj["TerrSelectFlag"]
      """  Use this field to display/update; replaces TerritorySelect  """  
      self.TerritorySelectDescription:str = obj["TerritorySelectDescription"]
      self.PeriodicityList:str = obj["PeriodicityList"]
      """  List of available Periodicity values  """  
      self.IntegrationFlag:bool = obj["IntegrationFlag"]
      """  Indicates Integration with financial package (like EuroFin)  """  
      self.GlbLink:str = obj["GlbLink"]
      """  Delimited list of GlbCompany, GlbCustNum and GlbShipto that is linking to this shipto  """  
      self.GlbFlag:bool = obj["GlbFlag"]
      """  Indicates if ShipTo is Global (Master or Linked)  """  
      self.PrimaryShipTo:bool = obj["PrimaryShipTo"]
      """  Used to indicate if primary shipto.  Updates Customer.ShipToNum field  """  
      self.PeriodicityDesc:str = obj["PeriodicityDesc"]
      self.CustID:str = obj["CustID"]
      self.CustNumBTName:str = obj["CustNumBTName"]
      """  The Bill To name of this customer. Will be used by the AR module for Invoices. This defaults to the Customer.Name but can be overrode by the user.  """  
      self.CustNumCustID:str = obj["CustNumCustID"]
      """  A user defined external customer ID.  This must be unique within the file.  This ID may be used in certain screen displays or reports where a full customer name is inappropriate. Therefore users should use meaningful characters as they would in any other master file. This master file key is a little different in that the user can change. This change is allowed because the system is not using the CustID as a foreign key in any other file.  Rather it uses the CustNum field which is assigned to th  """  
      self.CustNumName:str = obj["CustNumName"]
      """  The full name of the customer.  """  
      self.DeliveryTypeDescription:str = obj["DeliveryTypeDescription"]
      """  Description of delivery type  """  
      self.LanguageDescription:str = obj["LanguageDescription"]
      """  Language Name Description  """  
      self.MasterCustIDName:str = obj["MasterCustIDName"]
      """  The full name of the customer.  """  
      self.MasterCustIDBTName:str = obj["MasterCustIDBTName"]
      """  The Bill To name of this customer. Will be used by the AR module for Invoices. This defaults to the Customer.Name but can be overrode by the user.  """  
      self.MasterCustIDCustID:str = obj["MasterCustIDCustID"]
      """  A user defined external customer ID.  This must be unique within the file.  This ID may be used in certain screen displays or reports where a full customer name is inappropriate. Therefore users should use meaningful characters as they would in any other master file. This master file key is a little different in that the user can change. This change is allowed because the system is not using the CustID as a foreign key in any other file.  Rather it uses the CustNum field which is assigned to th  """  
      self.SalesRepName:str = obj["SalesRepName"]
      """  Name  """  
      self.ShipViaDescription:str = obj["ShipViaDescription"]
      """  Full description for the shipping company (carrier).  """  
      self.ShipViaWebDesc:str = obj["ShipViaWebDesc"]
      """  "External" Ship Via description for Customer Connect (StoreFront) selection.  """  
      self.TATaxAuthorityDescription:str = obj["TATaxAuthorityDescription"]
      """  Long Description of the tax authority code.  """  
      self.TaxRegionDescription:str = obj["TaxRegionDescription"]
      """  Full description for the Tax Region.  """  
      self.TerritoryTerritoryDesc:str = obj["TerritoryTerritoryDesc"]
      """  Description of the territory.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ShipToRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.CustNum:int = obj["CustNum"]
      """  The Customer.CustNum value of the customer that the record is related to.  """  
      self.ShipToNum:str = obj["ShipToNum"]
      """  The ID assigned by the user which makes this record unique for the customer.  When a customer is created a ShipTo record is automatically created by the system for that customer with a ShipToNum equal to NULL.  """  
      self.Name:str = obj["Name"]
      """  Name of the ShipTo. When creating new records the Customer.Name is used as a default.  """  
      self.Address1:str = obj["Address1"]
      """  The first line of the ShipTo address.  """  
      self.Address2:str = obj["Address2"]
      """  The second line of the ShipTo address.  """  
      self.Address3:str = obj["Address3"]
      """  The third line of the ShipTo address.  """  
      self.City:str = obj["City"]
      """  The city portion of the ShipTo address.  """  
      self.State:str = obj["State"]
      """  The state or province portion of the ShipTo address.  """  
      self.ZIP:str = obj["ZIP"]
      """  The zip or postal code portion of the ShipTo address.  """  
      self.Country:str = obj["Country"]
      """  The country portion of the ShipTo address.  """  
      self.ResaleID:str = obj["ResaleID"]
      """  The State Tax Identification Number. Used in Order Entry and prints on Sales Acknowledgements.  """  
      self.SalesRepCode:str = obj["SalesRepCode"]
      """  The SalesRep.SalesRepCode value of the default salesperson for the customer. Used as a default in Order Entry and Invoice entry. The SalesRep from the customer master is used as an initial default when creating new ship to.  """  
      self.TerritoryID:str = obj["TerritoryID"]
      """  The SalesTer.TerritoryID value of the territory the customer is assigned to.  """  
      self.ShipViaCode:str = obj["ShipViaCode"]
      """  The ShipVia.ShipViaCode value of the default ShipVia assigned to the customer. Used as a default in Order Entry, Shipping and Invoicing.  The shipvia from the customer record for this shipto is used as the initial default when creating new ShipTo records.  """  
      self.PrimSCon:int = obj["PrimSCon"]
      """  The CustCnt.ConNum of the default shipping contact for the ShipTo location. The primary shipping contact is used as a default in the shipping process.  """  
      self.FaxNum:str = obj["FaxNum"]
      """  The fax number for the ShipTo location. isplayed in Order entry when no shipping contact is given for or when contact has a blank phone number.  """  
      self.PhoneNum:str = obj["PhoneNum"]
      """  The business phone number for the ShipTo location. Displayed in Order entry when no shipping contact is given for or when contact has a blank phone number.  """  
      self.TaxExempt:str = obj["TaxExempt"]
      """  Determines whether or not the ShipTo location is normally exempt from sales tax. Used as a default in invoice entry.  If the field is non-blank it is considered exempt.   This code is totally user definable and no validation is required.  """  
      self.EDIShipNum:str = obj["EDIShipNum"]
      """  A mutually agreed upon value that links a customer's EDI shipto record (an N1 / ST) to the Manufacturing System DB ShipTo record.  """  
      self.CountryNum:int = obj["CountryNum"]
      """  The Country.CountryNum value of the country selected in the ShipTo.Country field.  """  
      self.LangNameID:str = obj["LangNameID"]
      """  The LangName.LangNameID value of the default Language assigned to the ShipTo location. This controls which language will be selected when extracting part descriptions from PartLangDesc table.  """  
      self.BorderCrossing:str = obj["BorderCrossing"]
      """  Area/city code from where goods cross the border. This field is intended for Intrastat reporting. The field can be blank to indicate the value from the Customer table. This field is only visible if ISSyst.EnableHarbour is set.  """  
      self.FormatStr:str = obj["FormatStr"]
      """  Optional custom address format for the ShipTo location.  """  
      self.TaxRegionCode:str = obj["TaxRegionCode"]
      """  Contains the TaxRgn.TaxRegionCode value of the customer's tax region for purposes of Sales Tax calculations.  """  
      self.EMailAddress:str = obj["EMailAddress"]
      """  The email address of the ShipTo location.  """  
      self.TerritorySelect:str = obj["TerritorySelect"]
      """   Determines how the ShipTo location should be assigned to a territory. There are 3 methods for Territory assignment in Ship-to:

Sync - Keep the ShipTo territory synchronized with the territory on the
       main customer record. (ShipTo.TerritoryID = Customer.TerritoryID)
Syst - Let the system (Get Territory) determine the territory to assign         to the ShipTo based on territory boundaries.
Lock - Check this method after assigning the territory manually to 
       prevent the system from attempting to reassign the territory.  """  
      self.PendingTerritoryID:str = obj["PendingTerritoryID"]
      """  The pending sales territory that the customer will be assigned to based on changes to the territory boundaries.  This functionality is only available with the CRM module.  """  
      self.CreatedByEDI:bool = obj["CreatedByEDI"]
      """  Determines whether or not the ShipTo record was created by an EDI transaction.  """  
      self.ExternalID:str = obj["ExternalID"]
      """  Unique identifier of the ShipTo from an external General Ledger interface such as the EuroFinancial integration.  """  
      self.TaxAuthorityCode:str = obj["TaxAuthorityCode"]
      """  The TaxAuthorityCd.TaxAuthorityCode value of the Tax Authority assigned to this ShipTo location.  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Disable this record from receiving global updates.  """  
      self.EDICode:str = obj["EDICode"]
      """  The Trading Partner ID that is used for incoming and outgoing EDI transactions.  """  
      self.DemandDeliveryDays:int = obj["DemandDeliveryDays"]
      """  Days to use in calculating the Order Detail Ship By date from the incoming need by date.  """  
      self.DemandDateType:str = obj["DemandDateType"]
      """   Indicates incoming date type.  Values are:
S - Shipping Date
N - Need By Date  """  
      self.DemandAddLeadTime:int = obj["DemandAddLeadTime"]
      """  The number of days from today to give a warning when adding a new order release record from an incoming shipping schedule.  """  
      self.DemandAddAction:str = obj["DemandAddAction"]
      """  Indicates what type of action to take if the add lead time is breeched.  Options are B (reject the change) or W (warning - alert that the lead time has been breeched but allow the record to be accepted).  """  
      self.DemandChangeLeadTime:int = obj["DemandChangeLeadTime"]
      """  The number of days from today to give a warning when changing an order release record from an incoming shipping schedule.  This does not include changes to quantity or dates.  """  
      self.DemandChangeAction:str = obj["DemandChangeAction"]
      """  Indicates what type of action to take if the change lead time is breeched.  Options are B (reject the change) or W (warning - alert that the lead time has been breeched but allow the record to be accepted).  """  
      self.DemandCancelLeadTime:int = obj["DemandCancelLeadTime"]
      """  The number of days from today to give a warning when canceling an order release record from an incoming shipping schedule.  """  
      self.DemandCancelAction:str = obj["DemandCancelAction"]
      """  Indicates what type of action to take if the cancel lead time is breeched.  Options are B (reject the change) or W (warning - alert that the lead time has been breeched but allow the record to be accepted).  """  
      self.DemandNewLineLeadTime:int = obj["DemandNewLineLeadTime"]
      """  The number of days from today to give a warning when adding a new order line record from an incoming shipping schedule.  """  
      self.DemandNewLineAction:str = obj["DemandNewLineAction"]
      """  Indicates what type of action to take if the new line lead time is breeched.  Options are B (reject the change) or W (warning - alert that the lead time has been breeched but allow the record to be accepted).  """  
      self.DemandQtyChangeLeadTime:int = obj["DemandQtyChangeLeadTime"]
      """  The number of days from today to give a warning when changing the quantity on an order release record from an incoming shipping schedule.  """  
      self.DemandQtyChangeAction:str = obj["DemandQtyChangeAction"]
      """  Indicates what type of action to take if the quantity change lead time is breeched.  Options are B (reject the change) or W (warning - alert that the lead time has been breeched but allow the record to be accepted).  """  
      self.DemandChangeDateLeadTime:int = obj["DemandChangeDateLeadTime"]
      """  The number of days from today to give a warning when changing the date on an order release record from an incoming shipping schedule.  """  
      self.DemandChangeDateAction:str = obj["DemandChangeDateAction"]
      """  Indicates what type of action to take if the change date lead time is breeched.  Options are B (reject the change) or W (warning - alert that the lead time has been breeched but allow the record to be accepted).  """  
      self.TradingPartnerName:str = obj["TradingPartnerName"]
      """  The trading partner name.  """  
      self.ResDelivery:bool = obj["ResDelivery"]
      """  Is this a residential delivery  """  
      self.SatDelivery:bool = obj["SatDelivery"]
      """  Is a Saturday delivery acceptable  """  
      self.SatPickup:bool = obj["SatPickup"]
      """  Is a Saturday pickup available  """  
      self.Hazmat:bool = obj["Hazmat"]
      """  Hazmat or Dangerous Goods delivery  """  
      self.DocOnly:bool = obj["DocOnly"]
      """  Documents Only delivery  """  
      self.RefNotes:str = obj["RefNotes"]
      """  Reference Notes for the delivery  """  
      self.ApplyChrg:bool = obj["ApplyChrg"]
      """  Apply Handling Charge to shipment  """  
      self.ChrgAmount:int = obj["ChrgAmount"]
      """  Handling Charge Amount  """  
      self.COD:bool = obj["COD"]
      """  Prefer COD delivery  """  
      self.CODFreight:bool = obj["CODFreight"]
      """  Add Freight COD Amount owed  """  
      self.CODCheck:bool = obj["CODCheck"]
      """  Cashier's Check or Money order is required on COD Delivery  """  
      self.CODAmount:int = obj["CODAmount"]
      """  Amount due on Cashier's check or money order  """  
      self.GroundType:str = obj["GroundType"]
      """  Valid Values are blank, "Any" (Any Payment), "GF" (Guaranteed Funds), or "Cash" (Currency)  """  
      self.NotifyFlag:bool = obj["NotifyFlag"]
      """  Indicates whether to send an email notification of delivery  """  
      self.NotifyEMail:str = obj["NotifyEMail"]
      """  The list of email address to notify about a delivery  """  
      self.DeclaredIns:bool = obj["DeclaredIns"]
      """  Flag to indicate that an insurance value was declared on delivery  """  
      self.DeclaredAmt:int = obj["DeclaredAmt"]
      """  Declared Insurance Amount  """  
      self.PeriodicityCode:int = obj["PeriodicityCode"]
      """  Periodicity Code.  Must be a valid code in the Periodicity table.  """  
      self.ServSignature:bool = obj["ServSignature"]
      """  Service delivery requires signature  """  
      self.ServAlert:bool = obj["ServAlert"]
      """  Service Priority Alert flag  """  
      self.ServHomeDel:bool = obj["ServHomeDel"]
      """  Service Home Delivery allowed  """  
      self.DeliveryType:str = obj["DeliveryType"]
      """  Service Home Delivery Type Code  """  
      self.ServDeliveryDate:str = obj["ServDeliveryDate"]
      """  Service Home Delivery date  """  
      self.ServPhone:str = obj["ServPhone"]
      """  Home delivery phone number  """  
      self.ServInstruct:str = obj["ServInstruct"]
      """  Service Delivery Instructions  """  
      self.ServRelease:bool = obj["ServRelease"]
      """  Service Signature release is on file  """  
      self.ServAuthNum:str = obj["ServAuthNum"]
      """  Service Signature Release authorization number  """  
      self.ServRef1:str = obj["ServRef1"]
      """  Service Reference 1  """  
      self.CommercialInvoice:bool = obj["CommercialInvoice"]
      """  Added for international shipping, Is a commercial invoice required  """  
      self.ServRef2:str = obj["ServRef2"]
      """  Service Reference 2  """  
      self.ShipExprtDeclartn:bool = obj["ShipExprtDeclartn"]
      """  Added for international shipping. Shipper's Export Declaration required  """  
      self.ServRef3:str = obj["ServRef3"]
      """  Service Reference 3  """  
      self.CertOfOrigin:bool = obj["CertOfOrigin"]
      """  For International shipping.  Certificate of Orgin required.  """  
      self.ServRef4:str = obj["ServRef4"]
      """  Service Reference 4  """  
      self.LetterOfInstr:bool = obj["LetterOfInstr"]
      """  For International shipping.  Shipper's Letter of Instruction.  """  
      self.ServRef5:str = obj["ServRef5"]
      """  Service Reference 5  """  
      self.HazardousShipment:bool = obj["HazardousShipment"]
      """  International Shipping - HazardousShipment  """  
      self.OverrideCarrier:bool = obj["OverrideCarrier"]
      """  Override Carrier Defaults.  If not checked then the customer values will be used if overriden else the Site values  """  
      self.IntrntlShip:bool = obj["IntrntlShip"]
      """  Is this an International shipment  """  
      self.OverrideService:bool = obj["OverrideService"]
      """  Override Service Options.  If not checked then the customer values will be used if overriden else the Site values  """  
      self.DemandUseCustomerValues:bool = obj["DemandUseCustomerValues"]
      """  Indicates if the demand fields from the customer should be used.  """  
      self.TaxRegReason:str = obj["TaxRegReason"]
      """  Tax Payer Registration Reason Code  """  
      self.EarlyBuffer:int = obj["EarlyBuffer"]
      """  Used to calculate on-time delivery performance rating  """  
      self.OrgRegCode:str = obj["OrgRegCode"]
      """  Organization Registration Code  """  
      self.LateBuffer:int = obj["LateBuffer"]
      """  Used to calculate on-time delivery performance rating  """  
      self.DemandUnitPriceDiff:bool = obj["DemandUnitPriceDiff"]
      """  Indicates if the unit price between the demand and the contract should be validated.  If this flag is checked, and the prices are different, when the demand is accepted a record will be written to the DemandLog table.  """  
      self.DemandUnitPriceDiffAction:str = obj["DemandUnitPriceDiffAction"]
      """  Indicates what type of action to take if the unit price between the demand and the contract is different.  Options are B (reject the change) or W (warning - alert that the unit price is different but allow the record to be accepted).  """  
      self.ExcFromVal:bool = obj["ExcFromVal"]
      """  A flag that indicates whether this address should be validated by the tax service.  """  
      self.AddressVal:bool = obj["AddressVal"]
      """  A flag indicating that an address has already been validated. This helps improve the performance of the bulk address validation process by allowing address that have already been validated to be skipped. This flag is set anytime a successful validation is performed, either by the bulk address validation or validation from the Customer form.  """  
      self.DemandCheckForPart:bool = obj["DemandCheckForPart"]
      """  Check for the part in the Part master.  """  
      self.DemandCheckForPartAction:str = obj["DemandCheckForPartAction"]
      """  Indicates what type of action to take if the Check for Part options is selected and the part is not in the part master file.  Options are B (reject the change) or W (warning - alert that the part is not in the part master but allow the record to be accepted).  """  
      self.FFID:str = obj["FFID"]
      """  International Shipping. Frieght Forwarder ID  """  
      self.FFAddress1:str = obj["FFAddress1"]
      """  International Shipping. The first line of the Frieght Forwarder main address.  """  
      self.FFAddress2:str = obj["FFAddress2"]
      """  International Shipping. The second line of the Frieght Forwarder main address.  """  
      self.FFCity:str = obj["FFCity"]
      """  Shipping, The city portion of the Frieght Forwarder main address.  """  
      self.FFState:str = obj["FFState"]
      """  International Shipping. The state or province portion of the shipment Frieght Forwarder main address.  """  
      self.FFZip:str = obj["FFZip"]
      """  International Shipping. The zip or postal code portion of the shipping Frieght Forwarder main address.  """  
      self.FFCountry:str = obj["FFCountry"]
      """  International shipping. The country of the Frieght Forwarder .  """  
      self.FFContact:str = obj["FFContact"]
      """  International Shipping. Frieght Forwarder Contact  """  
      self.FFCompName:str = obj["FFCompName"]
      """  International Shipping. Frieght Forwarder company name  """  
      self.FFPhoneNum:str = obj["FFPhoneNum"]
      """  International Shipping. Frieght Forwarder Phone number  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  Userid of user who made the last change to this record.  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  The date that the record was last changed  """  
      self.ChangeTime:int = obj["ChangeTime"]
      """  The time that the record was last change (seconds since midnight)  """  
      self.IndividualPackIDs:bool = obj["IndividualPackIDs"]
      """  Individual Pack IDs  """  
      self.FFCountryNum:int = obj["FFCountryNum"]
      """  Freight Forwarder Third address line  """  
      self.NonStdPkg:bool = obj["NonStdPkg"]
      """  Additional Handling flag  """  
      self.DeliveryConf:int = obj["DeliveryConf"]
      """   Determines the level of delivery confirmation.
1 - No Signature Required
2 - Adult Signature Required
3 - Confirmation Required
4 - Verbal Confirmation Required  """  
      self.AddlHdlgFlag:bool = obj["AddlHdlgFlag"]
      """  Non Standard Packaging  """  
      self.UPSQuantumView:bool = obj["UPSQuantumView"]
      """  UPS Quantum View  """  
      self.UPSQVShipFromName:str = obj["UPSQVShipFromName"]
      """  UPS Quantum View From Name  """  
      self.UPSQVMemo:str = obj["UPSQVMemo"]
      """  UPS Quantum View Memo  """  
      self.FFAddress3:str = obj["FFAddress3"]
      """  Freight Forwarder Country portion of the address  """  
      self.ETCAddrChg:bool = obj["ETCAddrChg"]
      """  Used to determine if an address changed because of the tax integration.  If true, the tax integration changed the address.  """  
      self.IsAlternate:bool = obj["IsAlternate"]
      """  Indicates if this is a alternate ShipTo. An alternate is a Shipto that is valid for this customer, but is defined/maintained by the "master" customer. See ShipTo.MasterCustNum/MasterShiptoNum.  """  
      self.MasterCustNum:int = obj["MasterCustNum"]
      """  Pertains to Alternate Shipto (IsAlternate). Contains the CustNum of the Shipto record that is the "Master". Changes made to the Master, are replicated to the alternates.  """  
      self.MasterShipToNum:str = obj["MasterShipToNum"]
      """  Pertains to Alternate Shipto (IsAlternate). Contains the ShipToNum of the Shipto record that is the "Master". Changes made to the Master, are replicated to the alternates.  """  
      self.DemandCheckForRev:bool = obj["DemandCheckForRev"]
      """  Check for Revision  """  
      self.DemandCheckForRevAction:str = obj["DemandCheckForRevAction"]
      """  Check for Revision Action  """  
      self.DemandCheckPartialShip:bool = obj["DemandCheckPartialShip"]
      """  Flag for checking partial Shipment for Demand Entry.  """  
      self.DemandCheckShipAction:str = obj["DemandCheckShipAction"]
      """  Check Partial Shipments Action: B =Stop  and W = Warning  """  
      self.DemandCloseRejSkd:bool = obj["DemandCloseRejSkd"]
      """  Define if at the moment of processing a demand the process should also close those rejected schedules that remain at demand entry  """  
      self.DemandPricing:str = obj["DemandPricing"]
      """  Defines if Internal Pricing or Customer Pricing will be used for checking price differences  """  
      self.PriceTolerance:int = obj["PriceTolerance"]
      """  Defines the tolerance for price difference validations  """  
      self.CheckDateCapPromise:bool = obj["CheckDateCapPromise"]
      """  If this flags is turned on then Demand CTP will automatically be executed as a part of the demand to order process.  """  
      self.CheckConfirmCapPromise:bool = obj["CheckConfirmCapPromise"]
      """  Confirm or not the Capable to Promise jobs from Demand Entry  """  
      self.CheckUpdateCapPromise:bool = obj["CheckUpdateCapPromise"]
      """  If checked, Updates the date in Demand Entry  """  
      self.DemandCapPromiseDate:str = obj["DemandCapPromiseDate"]
      """  This field will define the dates that will be validated as a part of the demand to order process. The valid values for this combo will be:  Need By (N), Ship By (S) and Both (B)  """  
      self.DemandCapPromiseAction:str = obj["DemandCapPromiseAction"]
      """  The value on this field will define the action to be taken when validating CTP. The valid values for this combo box will be: Warning (W) and Stop (S)  """  
      self.DemandCapPromiseUpdate:str = obj["DemandCapPromiseUpdate"]
      """   This field will define the dates that will be updated as a part of the demand to order process. The valid options will be:
Need By (N), Ship By (S) and Both  (B) NOTE .-In all the cases above the update of date will only be done if the CTP dates are beyond the dates on the file.  """  
      self.OTSmartString:bool = obj["OTSmartString"]
      """  When set to TRUE the smart string functionality will only be processed when the incoming demand is new. After it has been processed and saved, if a retransmission is sent the smart string values will be ignored.  """  
      self.LegalName:str = obj["LegalName"]
      """  Full Legal name  """  
      self.DemandCheckConfig:bool = obj["DemandCheckConfig"]
      """  If true then demand will be rejected when one or more demand lines are not configured properly. Applies only to Configurable parts.  """  
      self.DemandCheckCfgAction:str = obj["DemandCheckCfgAction"]
      """  Indicates the action to be taken if configuration values have not been entered for one or more demand lines.  """  
      self.WIWebShipTo:bool = obj["WIWebShipTo"]
      """  WIWebShipTo  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.AGApartment:str = obj["AGApartment"]
      """  AGApartment  """  
      self.AGExtraStreetNumber:str = obj["AGExtraStreetNumber"]
      """  AGExtraStreetNumber  """  
      self.AGFloor:str = obj["AGFloor"]
      """  AGFloor  """  
      self.AGGrossIncomeTaxID:str = obj["AGGrossIncomeTaxID"]
      """  AGGrossIncomeTaxID  """  
      self.AGLocationCode:str = obj["AGLocationCode"]
      """  AGLocationCode  """  
      self.AGNeighborhood:str = obj["AGNeighborhood"]
      """  AGNeighborhood  """  
      self.AGProvinceCode:str = obj["AGProvinceCode"]
      """  AGProvinceCode  """  
      self.AGStreet:str = obj["AGStreet"]
      """  AGStreet  """  
      self.AGStreetNumber:str = obj["AGStreetNumber"]
      """  AGStreetNumber  """  
      self.EntityUseCode:str = obj["EntityUseCode"]
      """  EntityUseCode  """  
      self.DemandCheckForRunOutPart:bool = obj["DemandCheckForRunOutPart"]
      """  Check if the part is a run out part.  """  
      self.DemandCheckForRunOutPartAction:str = obj["DemandCheckForRunOutPartAction"]
      """  Indicates what type of action to take if the Check for Run Out Part option is selected and the part is marked as a run out part.  Options are B (reject the change) or W (warning - alert that the part is marked as run out but allow the record to be accepted).  """  
      self.INExciseRegNumber:str = obj["INExciseRegNumber"]
      """  INExciseRegNumber  """  
      self.INVATNumber:str = obj["INVATNumber"]
      """  INVATNumber  """  
      self.INSTRegistration:str = obj["INSTRegistration"]
      """  INSTRegistration  """  
      self.MXCURP:str = obj["MXCURP"]
      """  MXCURP  """  
      self.MXMunicipio:str = obj["MXMunicipio"]
      """  MXMunicipio  """  
      self.MXFederalID:str = obj["MXFederalID"]
      """  MXFederalID  """  
      self.INTaxRegistrationID:str = obj["INTaxRegistrationID"]
      """  INTaxRegistrationID  """  
      self.PEUBIGEOCode:str = obj["PEUBIGEOCode"]
      """  Geographical Location Code  """  
      self.EORINumber:str = obj["EORINumber"]
      """  EORI Number  """  
      self.TaxValidationStatus:int = obj["TaxValidationStatus"]
      """  Tax ID Validation Status: Not Validated – 0, Valid – 1, Invalid – 2.  """  
      self.TaxValidationDate:str = obj["TaxValidationDate"]
      """  Tax Validation Date  """  
      self.HMRCTaxValidationLog:str = obj["HMRCTaxValidationLog"]
      """  HMRCTaxValidationLog  """  
      self.Inactive:bool = obj["Inactive"]
      """  Indicates if the record is inactive.  """  
      self.FSMRegionCode:str = obj["FSMRegionCode"]
      """  FSMRegionCode  """  
      self.FSMArea:str = obj["FSMArea"]
      """  FSMArea  """  
      self.COASegReferences:str = obj["COASegReferences"]
      """  List of fields which are referenced by COA segments.  """  
      self.ContactName:str = obj["ContactName"]
      """  Used for ContactTracker.  This is needed so the UI can relate the Contact Tracker tables together.  """  
      self.DspFormatStr:str = obj["DspFormatStr"]
      """  Display Format String  """  
      self.GlbFlag:bool = obj["GlbFlag"]
      """  Indicates if ShipTo is Global (Master or Linked)  """  
      self.GlbLink:str = obj["GlbLink"]
      """  Delimited list of GlbCompany, GlbCustNum and GlbShipto that is linking to this shipto  """  
      self.IntegrationFlag:bool = obj["IntegrationFlag"]
      """  Indicates Integration with financial package (like EuroFin)  """  
      self.IntRunChangeCountry:bool = obj["IntRunChangeCountry"]
      """  Flag used for integrations whether to run the on change country logic.  """  
      self.PeriodicityDesc:str = obj["PeriodicityDesc"]
      self.PeriodicityList:str = obj["PeriodicityList"]
      """  List of available Periodicity values  """  
      self.PrimaryShipTo:bool = obj["PrimaryShipTo"]
      """  Used to indicate if primary shipto.  Updates Customer.ShipToNum field  """  
      self.SalesTaxID:str = obj["SalesTaxID"]
      """  Sales Tax ID  """  
      self.ServiceTaxID:str = obj["ServiceTaxID"]
      """  Service Tax ID  """  
      self.TerritorySelectDescription:str = obj["TerritorySelectDescription"]
      self.TerrSelectFlag:str = obj["TerrSelectFlag"]
      """  Use this field to display/update; replaces TerritorySelect  """  
      self.AddrList:str = obj["AddrList"]
      """  Address in formatted delimited list  """  
      self.LanguageDescription:str = obj["LanguageDescription"]
      self.BitFlag:int = obj["BitFlag"]
      self.AGLocationDescription:str = obj["AGLocationDescription"]
      self.AGProvinceDescription:str = obj["AGProvinceDescription"]
      self.CountryISOCode:str = obj["CountryISOCode"]
      self.CountryEUMember:bool = obj["CountryEUMember"]
      self.CustNumName:str = obj["CustNumName"]
      self.CustNumCustID:str = obj["CustNumCustID"]
      self.CustNumBTName:str = obj["CustNumBTName"]
      self.DeliveryTypeDescription:str = obj["DeliveryTypeDescription"]
      self.MasterCustIDBTName:str = obj["MasterCustIDBTName"]
      self.MasterCustIDCustID:str = obj["MasterCustIDCustID"]
      self.MasterCustIDName:str = obj["MasterCustIDName"]
      self.SalesRepName:str = obj["SalesRepName"]
      self.ShipViaWebDesc:str = obj["ShipViaWebDesc"]
      self.ShipViaDescription:str = obj["ShipViaDescription"]
      self.TATaxAuthorityDescription:str = obj["TATaxAuthorityDescription"]
      self.TaxRegionDescription:str = obj["TaxRegionDescription"]
      self.TerritoryTerritoryDesc:str = obj["TerritoryTerritoryDesc"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class DeleteByID_input:
   """ Required : 
   custNum
   shipToNum
   """  
   def __init__(self, obj):
      self.custNum:int = obj["custNum"]
      self.shipToNum:str = obj["shipToNum"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_ShipToAttchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.CustNum:int = obj["CustNum"]
      self.ShipToNum:str = obj["ShipToNum"]
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

class Erp_Tablesets_ShipToLabExpRateRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.CustNum:int = obj["CustNum"]
      """  CustNum  """  
      self.ShipToNum:str = obj["ShipToNum"]
      """  ShipToNum  """  
      self.ExpenseCode:str = obj["ExpenseCode"]
      """  ExpenseCode  """  
      self.RateType:int = obj["RateType"]
      """  RateType  """  
      self.RateMultiplier:int = obj["RateMultiplier"]
      """  RateMultiplier  """  
      self.FixedRate:int = obj["FixedRate"]
      """  FixedRate  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.BitFlag:int = obj["BitFlag"]
      self.ShipToShipToNum:str = obj["ShipToShipToNum"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ShipToListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.CustNum:int = obj["CustNum"]
      """  The Customer.CustNum value of the customer that the record is related to.  """  
      self.ShipToNum:str = obj["ShipToNum"]
      """  The ID assigned by the user which makes this record unique for the customer.  When a customer is created a ShipTo record is automatically created by the system for that customer with a ShipToNum equal to NULL.  """  
      self.Name:str = obj["Name"]
      """  Name of the ShipTo. When creating new records the Customer.Name is used as a default.  """  
      self.Address1:str = obj["Address1"]
      """  The first line of the ShipTo address.  """  
      self.Address2:str = obj["Address2"]
      """  The second line of the ShipTo address.  """  
      self.Address3:str = obj["Address3"]
      """  The third line of the ShipTo address.  """  
      self.City:str = obj["City"]
      """  The city portion of the ShipTo address.  """  
      self.State:str = obj["State"]
      """  The state or province portion of the ShipTo address.  """  
      self.ZIP:str = obj["ZIP"]
      """  The zip or postal code portion of the ShipTo address.  """  
      self.Country:str = obj["Country"]
      """  The country portion of the ShipTo address.  """  
      self.ResaleID:str = obj["ResaleID"]
      """  The State Tax Identification Number. Used in Order Entry and prints on Sales Acknowledgements.  """  
      self.SalesRepCode:str = obj["SalesRepCode"]
      """  The SalesRep.SalesRepCode value of the default salesperson for the customer. Used as a default in Order Entry and Invoice entry. The SalesRep from the customer master is used as an initial default when creating new ship to.  """  
      self.TerritoryID:str = obj["TerritoryID"]
      """  The SalesTer.TerritoryID value of the territory the customer is assigned to.  """  
      self.ShipViaCode:str = obj["ShipViaCode"]
      """  The ShipVia.ShipViaCode value of the default ShipVia assigned to the customer. Used as a default in Order Entry, Shipping and Invoicing.  The shipvia from the customer record for this shipto is used as the initial default when creating new ShipTo records.  """  
      self.PrimSCon:int = obj["PrimSCon"]
      """  The CustCnt.ConNum of the default shipping contact for the ShipTo location. The primary shipping contact is used as a default in the shipping process.  """  
      self.FaxNum:str = obj["FaxNum"]
      """  The fax number for the ShipTo location. isplayed in Order entry when no shipping contact is given for or when contact has a blank phone number.  """  
      self.PhoneNum:str = obj["PhoneNum"]
      """  The business phone number for the ShipTo location. Displayed in Order entry when no shipping contact is given for or when contact has a blank phone number.  """  
      self.TaxExempt:str = obj["TaxExempt"]
      """  Determines whether or not the ShipTo location is normally exempt from sales tax. Used as a default in invoice entry.  If the field is non-blank it is considered exempt.   This code is totally user definable and no validation is required.  """  
      self.EDIShipNum:str = obj["EDIShipNum"]
      """  A mutually agreed upon value that links a customer's EDI shipto record (an N1 / ST) to the Manufacturing System DB ShipTo record.  """  
      self.CountryNum:int = obj["CountryNum"]
      """  The Country.CountryNum value of the country selected in the ShipTo.Country field.  """  
      self.LangNameID:str = obj["LangNameID"]
      """  The LangName.LangNameID value of the default Language assigned to the ShipTo location. This controls which language will be selected when extracting part descriptions from PartLangDesc table.  """  
      self.BorderCrossing:str = obj["BorderCrossing"]
      """  Area/city code from where goods cross the border. This field is intended for Intrastat reporting. The field can be blank to indicate the value from the Customer table. This field is only visible if ISSyst.EnableHarbour is set.  """  
      self.FormatStr:str = obj["FormatStr"]
      """  Optional custom address format for the ShipTo location.  """  
      self.TaxRegionCode:str = obj["TaxRegionCode"]
      """  Contains the TaxRgn.TaxRegionCode value of the customer's tax region for purposes of Sales Tax calculations.  """  
      self.EMailAddress:str = obj["EMailAddress"]
      """  The email address of the ShipTo location.  """  
      self.TerritorySelect:str = obj["TerritorySelect"]
      """   Determines how the ShipTo location should be assigned to a territory. There are 3 methods for Territory assignment in Ship-to:

Sync - Keep the ShipTo territory synchronized with the territory on the
       main customer record. (ShipTo.TerritoryID = Customer.TerritoryID)
Syst - Let the system (Get Territory) determine the territory to assign         to the ShipTo based on territory boundaries.
Lock - Check this method after assigning the territory manually to 
       prevent the system from attempting to reassign the territory.  """  
      self.PendingTerritoryID:str = obj["PendingTerritoryID"]
      """  The pending sales territory that the customer will be assigned to based on changes to the territory boundaries.  This functionality is only available with the CRM module.  """  
      self.CreatedByEDI:bool = obj["CreatedByEDI"]
      """  Determines whether or not the ShipTo record was created by an EDI transaction.  """  
      self.ExternalID:str = obj["ExternalID"]
      """  Unique identifier of the ShipTo from an external General Ledger interface such as the EuroFinancial integration.  """  
      self.TaxAuthorityCode:str = obj["TaxAuthorityCode"]
      """  The TaxAuthorityCd.TaxAuthorityCode value of the Tax Authority assigned to this ShipTo location.  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Disable this record from receiving global updates.  """  
      self.EDICode:str = obj["EDICode"]
      """  The Trading Partner ID that is used for incoming and outgoing EDI transactions.  """  
      self.DemandDeliveryDays:int = obj["DemandDeliveryDays"]
      """  Days to use in calculating the Order Detail Ship By date from the incoming need by date.  """  
      self.DemandDateType:str = obj["DemandDateType"]
      """   Indicates incoming date type.  Values are:
S - Shipping Date
N - Need By Date  """  
      self.DemandAddLeadTime:int = obj["DemandAddLeadTime"]
      """  The number of days from today to give a warning when adding a new order release record from an incoming shipping schedule.  """  
      self.DemandAddAction:str = obj["DemandAddAction"]
      """  Indicates what type of action to take if the add lead time is breeched.  Options are B (reject the change) or W (warning - alert that the lead time has been breeched but allow the record to be accepted).  """  
      self.DemandChangeLeadTime:int = obj["DemandChangeLeadTime"]
      """  The number of days from today to give a warning when changing an order release record from an incoming shipping schedule.  This does not include changes to quantity or dates.  """  
      self.DemandChangeAction:str = obj["DemandChangeAction"]
      """  Indicates what type of action to take if the change lead time is breeched.  Options are B (reject the change) or W (warning - alert that the lead time has been breeched but allow the record to be accepted).  """  
      self.DemandCancelLeadTime:int = obj["DemandCancelLeadTime"]
      """  The number of days from today to give a warning when canceling an order release record from an incoming shipping schedule.  """  
      self.DemandCancelAction:str = obj["DemandCancelAction"]
      """  Indicates what type of action to take if the cancel lead time is breeched.  Options are B (reject the change) or W (warning - alert that the lead time has been breeched but allow the record to be accepted).  """  
      self.DemandNewLineLeadTime:int = obj["DemandNewLineLeadTime"]
      """  The number of days from today to give a warning when adding a new order line record from an incoming shipping schedule.  """  
      self.DemandNewLineAction:str = obj["DemandNewLineAction"]
      """  Indicates what type of action to take if the new line lead time is breeched.  Options are B (reject the change) or W (warning - alert that the lead time has been breeched but allow the record to be accepted).  """  
      self.DemandQtyChangeLeadTime:int = obj["DemandQtyChangeLeadTime"]
      """  The number of days from today to give a warning when changing the quantity on an order release record from an incoming shipping schedule.  """  
      self.DemandQtyChangeAction:str = obj["DemandQtyChangeAction"]
      """  Indicates what type of action to take if the quantity change lead time is breeched.  Options are B (reject the change) or W (warning - alert that the lead time has been breeched but allow the record to be accepted).  """  
      self.DemandChangeDateLeadTime:int = obj["DemandChangeDateLeadTime"]
      """  The number of days from today to give a warning when changing the date on an order release record from an incoming shipping schedule.  """  
      self.DemandChangeDateAction:str = obj["DemandChangeDateAction"]
      """  Indicates what type of action to take if the change date lead time is breeched.  Options are B (reject the change) or W (warning - alert that the lead time has been breeched but allow the record to be accepted).  """  
      self.TradingPartnerName:str = obj["TradingPartnerName"]
      """  The trading partner name.  """  
      self.ResDelivery:bool = obj["ResDelivery"]
      """  Is this a residential delivery  """  
      self.SatDelivery:bool = obj["SatDelivery"]
      """  Is a Saturday delivery acceptable  """  
      self.SatPickup:bool = obj["SatPickup"]
      """  Is a Saturday pickup available  """  
      self.Hazmat:bool = obj["Hazmat"]
      """  Hazmat or Dangerous Goods delivery  """  
      self.DocOnly:bool = obj["DocOnly"]
      """  Documents Only delivery  """  
      self.RefNotes:str = obj["RefNotes"]
      """  Reference Notes for the delivery  """  
      self.ApplyChrg:bool = obj["ApplyChrg"]
      """  Apply Handling Charge to shipment  """  
      self.ChrgAmount:int = obj["ChrgAmount"]
      """  Handling Charge Amount  """  
      self.COD:bool = obj["COD"]
      """  Prefer COD delivery  """  
      self.CODFreight:bool = obj["CODFreight"]
      """  Add Freight COD Amount owed  """  
      self.CODCheck:bool = obj["CODCheck"]
      """  Cashier's Check or Money order is required on COD Delivery  """  
      self.CODAmount:int = obj["CODAmount"]
      """  Amount due on Cashier's check or money order  """  
      self.GroundType:str = obj["GroundType"]
      """  Valid Values are blank, "Any" (Any Payment), "GF" (Guaranteed Funds), or "Cash" (Currency)  """  
      self.NotifyFlag:bool = obj["NotifyFlag"]
      """  Indicates whether to send an email notification of delivery  """  
      self.NotifyEMail:str = obj["NotifyEMail"]
      """  The list of email address to notify about a delivery  """  
      self.DeclaredIns:bool = obj["DeclaredIns"]
      """  Flag to indicate that an insurance value was declared on delivery  """  
      self.DeclaredAmt:int = obj["DeclaredAmt"]
      """  Declared Insurance Amount  """  
      self.PeriodicityCode:int = obj["PeriodicityCode"]
      """  Periodicity Code.  Must be a valid code in the Periodicity table.  """  
      self.ServSignature:bool = obj["ServSignature"]
      """  Service delivery requires signature  """  
      self.ServAlert:bool = obj["ServAlert"]
      """  Service Priority Alert flag  """  
      self.ServHomeDel:bool = obj["ServHomeDel"]
      """  Service Home Delivery allowed  """  
      self.DeliveryType:str = obj["DeliveryType"]
      """  Service Home Delivery Type Code  """  
      self.ServDeliveryDate:str = obj["ServDeliveryDate"]
      """  Service Home Delivery date  """  
      self.ServPhone:str = obj["ServPhone"]
      """  Home delivery phone number  """  
      self.ServInstruct:str = obj["ServInstruct"]
      """  Service Delivery Instructions  """  
      self.ServRelease:bool = obj["ServRelease"]
      """  Service Signature release is on file  """  
      self.ServAuthNum:str = obj["ServAuthNum"]
      """  Service Signature Release authorization number  """  
      self.ServRef1:str = obj["ServRef1"]
      """  Service Reference 1  """  
      self.CommercialInvoice:bool = obj["CommercialInvoice"]
      """  Added for international shipping, Is a commercial invoice required  """  
      self.ServRef2:str = obj["ServRef2"]
      """  Service Reference 2  """  
      self.ShipExprtDeclartn:bool = obj["ShipExprtDeclartn"]
      """  Added for international shipping. Shipper's Export Declaration required  """  
      self.ServRef3:str = obj["ServRef3"]
      """  Service Reference 3  """  
      self.CertOfOrigin:bool = obj["CertOfOrigin"]
      """  For International shipping.  Certificate of Orgin required.  """  
      self.ServRef4:str = obj["ServRef4"]
      """  Service Reference 4  """  
      self.LetterOfInstr:bool = obj["LetterOfInstr"]
      """  For International shipping.  Shipper's Letter of Instruction.  """  
      self.ServRef5:str = obj["ServRef5"]
      """  Service Reference 5  """  
      self.HazardousShipment:bool = obj["HazardousShipment"]
      """  International Shipping - HazardousShipment  """  
      self.OverrideCarrier:bool = obj["OverrideCarrier"]
      """  Override Carrier Defaults.  If not checked then the customer values will be used if overriden else the Site values  """  
      self.IntrntlShip:bool = obj["IntrntlShip"]
      """  Is this an International shipment  """  
      self.OverrideService:bool = obj["OverrideService"]
      """  Override Service Options.  If not checked then the customer values will be used if overriden else the Site values  """  
      self.DemandUseCustomerValues:bool = obj["DemandUseCustomerValues"]
      """  Indicates if the demand fields from the customer should be used.  """  
      self.TaxRegReason:str = obj["TaxRegReason"]
      """  Tax Payer Registration Reason Code  """  
      self.EarlyBuffer:int = obj["EarlyBuffer"]
      """  Used to calculate on-time delivery performance rating  """  
      self.OrgRegCode:str = obj["OrgRegCode"]
      """  Organization Registration Code  """  
      self.LateBuffer:int = obj["LateBuffer"]
      """  Used to calculate on-time delivery performance rating  """  
      self.DemandUnitPriceDiff:bool = obj["DemandUnitPriceDiff"]
      """  Indicates if the unit price between the demand and the contract should be validated.  If this flag is checked, and the prices are different, when the demand is accepted a record will be written to the DemandLog table.  """  
      self.DemandUnitPriceDiffAction:str = obj["DemandUnitPriceDiffAction"]
      """  Indicates what type of action to take if the unit price between the demand and the contract is different.  Options are B (reject the change) or W (warning - alert that the unit price is different but allow the record to be accepted).  """  
      self.ExcFromVal:bool = obj["ExcFromVal"]
      """  A flag that indicates whether this address should be validated by the tax service.  """  
      self.AddressVal:bool = obj["AddressVal"]
      """  A flag indicating that an address has already been validated. This helps improve the performance of the bulk address validation process by allowing address that have already been validated to be skipped. This flag is set anytime a successful validation is performed, either by the bulk address validation or validation from the Customer form.  """  
      self.DemandCheckForPart:bool = obj["DemandCheckForPart"]
      """  Check for the part in the Part master.  """  
      self.DemandCheckForPartAction:str = obj["DemandCheckForPartAction"]
      """  Indicates what type of action to take if the Check for Part options is selected and the part is not in the part master file.  Options are B (reject the change) or W (warning - alert that the part is not in the part master but allow the record to be accepted).  """  
      self.FFID:str = obj["FFID"]
      """  International Shipping. Frieght Forwarder ID  """  
      self.FFAddress1:str = obj["FFAddress1"]
      """  International Shipping. The first line of the Frieght Forwarder main address.  """  
      self.FFAddress2:str = obj["FFAddress2"]
      """  International Shipping. The second line of the Frieght Forwarder main address.  """  
      self.FFCity:str = obj["FFCity"]
      """  Shipping, The city portion of the Frieght Forwarder main address.  """  
      self.FFState:str = obj["FFState"]
      """  International Shipping. The state or province portion of the shipment Frieght Forwarder main address.  """  
      self.FFZip:str = obj["FFZip"]
      """  International Shipping. The zip or postal code portion of the shipping Frieght Forwarder main address.  """  
      self.FFCountry:str = obj["FFCountry"]
      """  International shipping. The country of the Frieght Forwarder .  """  
      self.FFContact:str = obj["FFContact"]
      """  International Shipping. Frieght Forwarder Contact  """  
      self.FFCompName:str = obj["FFCompName"]
      """  International Shipping. Frieght Forwarder company name  """  
      self.FFPhoneNum:str = obj["FFPhoneNum"]
      """  International Shipping. Frieght Forwarder Phone number  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  Userid of user who made the last change to this record.  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  The date that the record was last changed  """  
      self.ChangeTime:int = obj["ChangeTime"]
      """  The time that the record was last change (seconds since midnight)  """  
      self.IndividualPackIDs:bool = obj["IndividualPackIDs"]
      """  Individual Pack IDs  """  
      self.FFCountryNum:int = obj["FFCountryNum"]
      """  Freight Forwarder Third address line  """  
      self.NonStdPkg:bool = obj["NonStdPkg"]
      """  Additional Handling flag  """  
      self.DeliveryConf:int = obj["DeliveryConf"]
      """   Determines the level of delivery confirmation.
1 - No Signature Required
2 - Adult Signature Required
3 - Confirmation Required
4 - Verbal Confirmation Required  """  
      self.AddlHdlgFlag:bool = obj["AddlHdlgFlag"]
      """  Non Standard Packaging  """  
      self.UPSQuantumView:bool = obj["UPSQuantumView"]
      """  UPS Quantum View  """  
      self.UPSQVShipFromName:str = obj["UPSQVShipFromName"]
      """  UPS Quantum View From Name  """  
      self.UPSQVMemo:str = obj["UPSQVMemo"]
      """  UPS Quantum View Memo  """  
      self.FFAddress3:str = obj["FFAddress3"]
      """  Freight Forwarder Country portion of the address  """  
      self.ETCAddrChg:bool = obj["ETCAddrChg"]
      """  Used to determine if an address changed because of the tax integration.  If true, the tax integration changed the address.  """  
      self.IsAlternate:bool = obj["IsAlternate"]
      """  Indicates if this is a alternate ShipTo. An alternate is a Shipto that is valid for this customer, but is defined/maintained by the "master" customer. See ShipTo.MasterCustNum/MasterShiptoNum.  """  
      self.MasterCustNum:int = obj["MasterCustNum"]
      """  Pertains to Alternate Shipto (IsAlternate). Contains the CustNum of the Shipto record that is the "Master". Changes made to the Master, are replicated to the alternates.  """  
      self.MasterShipToNum:str = obj["MasterShipToNum"]
      """  Pertains to Alternate Shipto (IsAlternate). Contains the ShipToNum of the Shipto record that is the "Master". Changes made to the Master, are replicated to the alternates.  """  
      self.DemandCheckForRev:bool = obj["DemandCheckForRev"]
      """  Check for Revision  """  
      self.DemandCheckForRevAction:str = obj["DemandCheckForRevAction"]
      """  Check for Revision Action  """  
      self.DemandCheckPartialShip:bool = obj["DemandCheckPartialShip"]
      """  Flag for checking partial Shipment for Demand Entry.  """  
      self.DemandCheckShipAction:str = obj["DemandCheckShipAction"]
      """  Check Partial Shipments Action: B =Stop  and W = Warning  """  
      self.DemandCloseRejSkd:bool = obj["DemandCloseRejSkd"]
      """  Define if at the moment of processing a demand the process should also close those rejected schedules that remain at demand entry  """  
      self.DemandPricing:str = obj["DemandPricing"]
      """  Defines if Internal Pricing or Customer Pricing will be used for checking price differences  """  
      self.PriceTolerance:int = obj["PriceTolerance"]
      """  Defines the tolerance for price difference validations  """  
      self.CheckDateCapPromise:bool = obj["CheckDateCapPromise"]
      """  If this flags is turned on then Demand CTP will automatically be executed as a part of the demand to order process.  """  
      self.CheckConfirmCapPromise:bool = obj["CheckConfirmCapPromise"]
      """  Confirm or not the Capable to Promise jobs from Demand Entry  """  
      self.CheckUpdateCapPromise:bool = obj["CheckUpdateCapPromise"]
      """  If checked, Updates the date in Demand Entry  """  
      self.DemandCapPromiseDate:str = obj["DemandCapPromiseDate"]
      """  This field will define the dates that will be validated as a part of the demand to order process. The valid values for this combo will be:  Need By (N), Ship By (S) and Both (B)  """  
      self.DemandCapPromiseAction:str = obj["DemandCapPromiseAction"]
      """  The value on this field will define the action to be taken when validating CTP. The valid values for this combo box will be: Warning (W) and Stop (S)  """  
      self.DemandCapPromiseUpdate:str = obj["DemandCapPromiseUpdate"]
      """   This field will define the dates that will be updated as a part of the demand to order process. The valid options will be:
Need By (N), Ship By (S) and Both  (B) NOTE .-In all the cases above the update of date will only be done if the CTP dates are beyond the dates on the file.  """  
      self.OTSmartString:bool = obj["OTSmartString"]
      """  When set to TRUE the smart string functionality will only be processed when the incoming demand is new. After it has been processed and saved, if a retransmission is sent the smart string values will be ignored.  """  
      self.LegalName:str = obj["LegalName"]
      """  Full Legal name  """  
      self.DemandCheckConfig:bool = obj["DemandCheckConfig"]
      """  If true then demand will be rejected when one or more demand lines are not configured properly. Applies only to Configurable parts.  """  
      self.DemandCheckCfgAction:str = obj["DemandCheckCfgAction"]
      """  Indicates the action to be taken if configuration values have not been entered for one or more demand lines.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.AddrList:str = obj["AddrList"]
      """  Address in formatted delimited list  """  
      self.ContactName:str = obj["ContactName"]
      """  Used for ContactTracker.  This is needed so the UI can relate the Contact Tracker tables together.  """  
      self.DspFormatStr:str = obj["DspFormatStr"]
      """  Display Format String  """  
      self.TerrSelectFlag:str = obj["TerrSelectFlag"]
      """  Use this field to display/update; replaces TerritorySelect  """  
      self.TerritorySelectDescription:str = obj["TerritorySelectDescription"]
      self.PeriodicityList:str = obj["PeriodicityList"]
      """  List of available Periodicity values  """  
      self.IntegrationFlag:bool = obj["IntegrationFlag"]
      """  Indicates Integration with financial package (like EuroFin)  """  
      self.GlbLink:str = obj["GlbLink"]
      """  Delimited list of GlbCompany, GlbCustNum and GlbShipto that is linking to this shipto  """  
      self.GlbFlag:bool = obj["GlbFlag"]
      """  Indicates if ShipTo is Global (Master or Linked)  """  
      self.PrimaryShipTo:bool = obj["PrimaryShipTo"]
      """  Used to indicate if primary shipto.  Updates Customer.ShipToNum field  """  
      self.PeriodicityDesc:str = obj["PeriodicityDesc"]
      self.CustID:str = obj["CustID"]
      self.CustNumBTName:str = obj["CustNumBTName"]
      """  The Bill To name of this customer. Will be used by the AR module for Invoices. This defaults to the Customer.Name but can be overrode by the user.  """  
      self.CustNumCustID:str = obj["CustNumCustID"]
      """  A user defined external customer ID.  This must be unique within the file.  This ID may be used in certain screen displays or reports where a full customer name is inappropriate. Therefore users should use meaningful characters as they would in any other master file. This master file key is a little different in that the user can change. This change is allowed because the system is not using the CustID as a foreign key in any other file.  Rather it uses the CustNum field which is assigned to th  """  
      self.CustNumName:str = obj["CustNumName"]
      """  The full name of the customer.  """  
      self.DeliveryTypeDescription:str = obj["DeliveryTypeDescription"]
      """  Description of delivery type  """  
      self.LanguageDescription:str = obj["LanguageDescription"]
      """  Language Name Description  """  
      self.MasterCustIDName:str = obj["MasterCustIDName"]
      """  The full name of the customer.  """  
      self.MasterCustIDBTName:str = obj["MasterCustIDBTName"]
      """  The Bill To name of this customer. Will be used by the AR module for Invoices. This defaults to the Customer.Name but can be overrode by the user.  """  
      self.MasterCustIDCustID:str = obj["MasterCustIDCustID"]
      """  A user defined external customer ID.  This must be unique within the file.  This ID may be used in certain screen displays or reports where a full customer name is inappropriate. Therefore users should use meaningful characters as they would in any other master file. This master file key is a little different in that the user can change. This change is allowed because the system is not using the CustID as a foreign key in any other file.  Rather it uses the CustNum field which is assigned to th  """  
      self.SalesRepName:str = obj["SalesRepName"]
      """  Name  """  
      self.ShipViaDescription:str = obj["ShipViaDescription"]
      """  Full description for the shipping company (carrier).  """  
      self.ShipViaWebDesc:str = obj["ShipViaWebDesc"]
      """  "External" Ship Via description for Customer Connect (StoreFront) selection.  """  
      self.TATaxAuthorityDescription:str = obj["TATaxAuthorityDescription"]
      """  Long Description of the tax authority code.  """  
      self.TaxRegionDescription:str = obj["TaxRegionDescription"]
      """  Full description for the Tax Region.  """  
      self.TerritoryTerritoryDesc:str = obj["TerritoryTerritoryDesc"]
      """  Description of the territory.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ShipToListTableset:
   def __init__(self, obj):
      self.ShipToList:list[Erp_Tablesets_ShipToListRow] = obj["ShipToList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_ShipToRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.CustNum:int = obj["CustNum"]
      """  The Customer.CustNum value of the customer that the record is related to.  """  
      self.ShipToNum:str = obj["ShipToNum"]
      """  The ID assigned by the user which makes this record unique for the customer.  When a customer is created a ShipTo record is automatically created by the system for that customer with a ShipToNum equal to NULL.  """  
      self.Name:str = obj["Name"]
      """  Name of the ShipTo. When creating new records the Customer.Name is used as a default.  """  
      self.Address1:str = obj["Address1"]
      """  The first line of the ShipTo address.  """  
      self.Address2:str = obj["Address2"]
      """  The second line of the ShipTo address.  """  
      self.Address3:str = obj["Address3"]
      """  The third line of the ShipTo address.  """  
      self.City:str = obj["City"]
      """  The city portion of the ShipTo address.  """  
      self.State:str = obj["State"]
      """  The state or province portion of the ShipTo address.  """  
      self.ZIP:str = obj["ZIP"]
      """  The zip or postal code portion of the ShipTo address.  """  
      self.Country:str = obj["Country"]
      """  The country portion of the ShipTo address.  """  
      self.ResaleID:str = obj["ResaleID"]
      """  The State Tax Identification Number. Used in Order Entry and prints on Sales Acknowledgements.  """  
      self.SalesRepCode:str = obj["SalesRepCode"]
      """  The SalesRep.SalesRepCode value of the default salesperson for the customer. Used as a default in Order Entry and Invoice entry. The SalesRep from the customer master is used as an initial default when creating new ship to.  """  
      self.TerritoryID:str = obj["TerritoryID"]
      """  The SalesTer.TerritoryID value of the territory the customer is assigned to.  """  
      self.ShipViaCode:str = obj["ShipViaCode"]
      """  The ShipVia.ShipViaCode value of the default ShipVia assigned to the customer. Used as a default in Order Entry, Shipping and Invoicing.  The shipvia from the customer record for this shipto is used as the initial default when creating new ShipTo records.  """  
      self.PrimSCon:int = obj["PrimSCon"]
      """  The CustCnt.ConNum of the default shipping contact for the ShipTo location. The primary shipping contact is used as a default in the shipping process.  """  
      self.FaxNum:str = obj["FaxNum"]
      """  The fax number for the ShipTo location. isplayed in Order entry when no shipping contact is given for or when contact has a blank phone number.  """  
      self.PhoneNum:str = obj["PhoneNum"]
      """  The business phone number for the ShipTo location. Displayed in Order entry when no shipping contact is given for or when contact has a blank phone number.  """  
      self.TaxExempt:str = obj["TaxExempt"]
      """  Determines whether or not the ShipTo location is normally exempt from sales tax. Used as a default in invoice entry.  If the field is non-blank it is considered exempt.   This code is totally user definable and no validation is required.  """  
      self.EDIShipNum:str = obj["EDIShipNum"]
      """  A mutually agreed upon value that links a customer's EDI shipto record (an N1 / ST) to the Manufacturing System DB ShipTo record.  """  
      self.CountryNum:int = obj["CountryNum"]
      """  The Country.CountryNum value of the country selected in the ShipTo.Country field.  """  
      self.LangNameID:str = obj["LangNameID"]
      """  The LangName.LangNameID value of the default Language assigned to the ShipTo location. This controls which language will be selected when extracting part descriptions from PartLangDesc table.  """  
      self.BorderCrossing:str = obj["BorderCrossing"]
      """  Area/city code from where goods cross the border. This field is intended for Intrastat reporting. The field can be blank to indicate the value from the Customer table. This field is only visible if ISSyst.EnableHarbour is set.  """  
      self.FormatStr:str = obj["FormatStr"]
      """  Optional custom address format for the ShipTo location.  """  
      self.TaxRegionCode:str = obj["TaxRegionCode"]
      """  Contains the TaxRgn.TaxRegionCode value of the customer's tax region for purposes of Sales Tax calculations.  """  
      self.EMailAddress:str = obj["EMailAddress"]
      """  The email address of the ShipTo location.  """  
      self.TerritorySelect:str = obj["TerritorySelect"]
      """   Determines how the ShipTo location should be assigned to a territory. There are 3 methods for Territory assignment in Ship-to:

Sync - Keep the ShipTo territory synchronized with the territory on the
       main customer record. (ShipTo.TerritoryID = Customer.TerritoryID)
Syst - Let the system (Get Territory) determine the territory to assign         to the ShipTo based on territory boundaries.
Lock - Check this method after assigning the territory manually to 
       prevent the system from attempting to reassign the territory.  """  
      self.PendingTerritoryID:str = obj["PendingTerritoryID"]
      """  The pending sales territory that the customer will be assigned to based on changes to the territory boundaries.  This functionality is only available with the CRM module.  """  
      self.CreatedByEDI:bool = obj["CreatedByEDI"]
      """  Determines whether or not the ShipTo record was created by an EDI transaction.  """  
      self.ExternalID:str = obj["ExternalID"]
      """  Unique identifier of the ShipTo from an external General Ledger interface such as the EuroFinancial integration.  """  
      self.TaxAuthorityCode:str = obj["TaxAuthorityCode"]
      """  The TaxAuthorityCd.TaxAuthorityCode value of the Tax Authority assigned to this ShipTo location.  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Disable this record from receiving global updates.  """  
      self.EDICode:str = obj["EDICode"]
      """  The Trading Partner ID that is used for incoming and outgoing EDI transactions.  """  
      self.DemandDeliveryDays:int = obj["DemandDeliveryDays"]
      """  Days to use in calculating the Order Detail Ship By date from the incoming need by date.  """  
      self.DemandDateType:str = obj["DemandDateType"]
      """   Indicates incoming date type.  Values are:
S - Shipping Date
N - Need By Date  """  
      self.DemandAddLeadTime:int = obj["DemandAddLeadTime"]
      """  The number of days from today to give a warning when adding a new order release record from an incoming shipping schedule.  """  
      self.DemandAddAction:str = obj["DemandAddAction"]
      """  Indicates what type of action to take if the add lead time is breeched.  Options are B (reject the change) or W (warning - alert that the lead time has been breeched but allow the record to be accepted).  """  
      self.DemandChangeLeadTime:int = obj["DemandChangeLeadTime"]
      """  The number of days from today to give a warning when changing an order release record from an incoming shipping schedule.  This does not include changes to quantity or dates.  """  
      self.DemandChangeAction:str = obj["DemandChangeAction"]
      """  Indicates what type of action to take if the change lead time is breeched.  Options are B (reject the change) or W (warning - alert that the lead time has been breeched but allow the record to be accepted).  """  
      self.DemandCancelLeadTime:int = obj["DemandCancelLeadTime"]
      """  The number of days from today to give a warning when canceling an order release record from an incoming shipping schedule.  """  
      self.DemandCancelAction:str = obj["DemandCancelAction"]
      """  Indicates what type of action to take if the cancel lead time is breeched.  Options are B (reject the change) or W (warning - alert that the lead time has been breeched but allow the record to be accepted).  """  
      self.DemandNewLineLeadTime:int = obj["DemandNewLineLeadTime"]
      """  The number of days from today to give a warning when adding a new order line record from an incoming shipping schedule.  """  
      self.DemandNewLineAction:str = obj["DemandNewLineAction"]
      """  Indicates what type of action to take if the new line lead time is breeched.  Options are B (reject the change) or W (warning - alert that the lead time has been breeched but allow the record to be accepted).  """  
      self.DemandQtyChangeLeadTime:int = obj["DemandQtyChangeLeadTime"]
      """  The number of days from today to give a warning when changing the quantity on an order release record from an incoming shipping schedule.  """  
      self.DemandQtyChangeAction:str = obj["DemandQtyChangeAction"]
      """  Indicates what type of action to take if the quantity change lead time is breeched.  Options are B (reject the change) or W (warning - alert that the lead time has been breeched but allow the record to be accepted).  """  
      self.DemandChangeDateLeadTime:int = obj["DemandChangeDateLeadTime"]
      """  The number of days from today to give a warning when changing the date on an order release record from an incoming shipping schedule.  """  
      self.DemandChangeDateAction:str = obj["DemandChangeDateAction"]
      """  Indicates what type of action to take if the change date lead time is breeched.  Options are B (reject the change) or W (warning - alert that the lead time has been breeched but allow the record to be accepted).  """  
      self.TradingPartnerName:str = obj["TradingPartnerName"]
      """  The trading partner name.  """  
      self.ResDelivery:bool = obj["ResDelivery"]
      """  Is this a residential delivery  """  
      self.SatDelivery:bool = obj["SatDelivery"]
      """  Is a Saturday delivery acceptable  """  
      self.SatPickup:bool = obj["SatPickup"]
      """  Is a Saturday pickup available  """  
      self.Hazmat:bool = obj["Hazmat"]
      """  Hazmat or Dangerous Goods delivery  """  
      self.DocOnly:bool = obj["DocOnly"]
      """  Documents Only delivery  """  
      self.RefNotes:str = obj["RefNotes"]
      """  Reference Notes for the delivery  """  
      self.ApplyChrg:bool = obj["ApplyChrg"]
      """  Apply Handling Charge to shipment  """  
      self.ChrgAmount:int = obj["ChrgAmount"]
      """  Handling Charge Amount  """  
      self.COD:bool = obj["COD"]
      """  Prefer COD delivery  """  
      self.CODFreight:bool = obj["CODFreight"]
      """  Add Freight COD Amount owed  """  
      self.CODCheck:bool = obj["CODCheck"]
      """  Cashier's Check or Money order is required on COD Delivery  """  
      self.CODAmount:int = obj["CODAmount"]
      """  Amount due on Cashier's check or money order  """  
      self.GroundType:str = obj["GroundType"]
      """  Valid Values are blank, "Any" (Any Payment), "GF" (Guaranteed Funds), or "Cash" (Currency)  """  
      self.NotifyFlag:bool = obj["NotifyFlag"]
      """  Indicates whether to send an email notification of delivery  """  
      self.NotifyEMail:str = obj["NotifyEMail"]
      """  The list of email address to notify about a delivery  """  
      self.DeclaredIns:bool = obj["DeclaredIns"]
      """  Flag to indicate that an insurance value was declared on delivery  """  
      self.DeclaredAmt:int = obj["DeclaredAmt"]
      """  Declared Insurance Amount  """  
      self.PeriodicityCode:int = obj["PeriodicityCode"]
      """  Periodicity Code.  Must be a valid code in the Periodicity table.  """  
      self.ServSignature:bool = obj["ServSignature"]
      """  Service delivery requires signature  """  
      self.ServAlert:bool = obj["ServAlert"]
      """  Service Priority Alert flag  """  
      self.ServHomeDel:bool = obj["ServHomeDel"]
      """  Service Home Delivery allowed  """  
      self.DeliveryType:str = obj["DeliveryType"]
      """  Service Home Delivery Type Code  """  
      self.ServDeliveryDate:str = obj["ServDeliveryDate"]
      """  Service Home Delivery date  """  
      self.ServPhone:str = obj["ServPhone"]
      """  Home delivery phone number  """  
      self.ServInstruct:str = obj["ServInstruct"]
      """  Service Delivery Instructions  """  
      self.ServRelease:bool = obj["ServRelease"]
      """  Service Signature release is on file  """  
      self.ServAuthNum:str = obj["ServAuthNum"]
      """  Service Signature Release authorization number  """  
      self.ServRef1:str = obj["ServRef1"]
      """  Service Reference 1  """  
      self.CommercialInvoice:bool = obj["CommercialInvoice"]
      """  Added for international shipping, Is a commercial invoice required  """  
      self.ServRef2:str = obj["ServRef2"]
      """  Service Reference 2  """  
      self.ShipExprtDeclartn:bool = obj["ShipExprtDeclartn"]
      """  Added for international shipping. Shipper's Export Declaration required  """  
      self.ServRef3:str = obj["ServRef3"]
      """  Service Reference 3  """  
      self.CertOfOrigin:bool = obj["CertOfOrigin"]
      """  For International shipping.  Certificate of Orgin required.  """  
      self.ServRef4:str = obj["ServRef4"]
      """  Service Reference 4  """  
      self.LetterOfInstr:bool = obj["LetterOfInstr"]
      """  For International shipping.  Shipper's Letter of Instruction.  """  
      self.ServRef5:str = obj["ServRef5"]
      """  Service Reference 5  """  
      self.HazardousShipment:bool = obj["HazardousShipment"]
      """  International Shipping - HazardousShipment  """  
      self.OverrideCarrier:bool = obj["OverrideCarrier"]
      """  Override Carrier Defaults.  If not checked then the customer values will be used if overriden else the Site values  """  
      self.IntrntlShip:bool = obj["IntrntlShip"]
      """  Is this an International shipment  """  
      self.OverrideService:bool = obj["OverrideService"]
      """  Override Service Options.  If not checked then the customer values will be used if overriden else the Site values  """  
      self.DemandUseCustomerValues:bool = obj["DemandUseCustomerValues"]
      """  Indicates if the demand fields from the customer should be used.  """  
      self.TaxRegReason:str = obj["TaxRegReason"]
      """  Tax Payer Registration Reason Code  """  
      self.EarlyBuffer:int = obj["EarlyBuffer"]
      """  Used to calculate on-time delivery performance rating  """  
      self.OrgRegCode:str = obj["OrgRegCode"]
      """  Organization Registration Code  """  
      self.LateBuffer:int = obj["LateBuffer"]
      """  Used to calculate on-time delivery performance rating  """  
      self.DemandUnitPriceDiff:bool = obj["DemandUnitPriceDiff"]
      """  Indicates if the unit price between the demand and the contract should be validated.  If this flag is checked, and the prices are different, when the demand is accepted a record will be written to the DemandLog table.  """  
      self.DemandUnitPriceDiffAction:str = obj["DemandUnitPriceDiffAction"]
      """  Indicates what type of action to take if the unit price between the demand and the contract is different.  Options are B (reject the change) or W (warning - alert that the unit price is different but allow the record to be accepted).  """  
      self.ExcFromVal:bool = obj["ExcFromVal"]
      """  A flag that indicates whether this address should be validated by the tax service.  """  
      self.AddressVal:bool = obj["AddressVal"]
      """  A flag indicating that an address has already been validated. This helps improve the performance of the bulk address validation process by allowing address that have already been validated to be skipped. This flag is set anytime a successful validation is performed, either by the bulk address validation or validation from the Customer form.  """  
      self.DemandCheckForPart:bool = obj["DemandCheckForPart"]
      """  Check for the part in the Part master.  """  
      self.DemandCheckForPartAction:str = obj["DemandCheckForPartAction"]
      """  Indicates what type of action to take if the Check for Part options is selected and the part is not in the part master file.  Options are B (reject the change) or W (warning - alert that the part is not in the part master but allow the record to be accepted).  """  
      self.FFID:str = obj["FFID"]
      """  International Shipping. Frieght Forwarder ID  """  
      self.FFAddress1:str = obj["FFAddress1"]
      """  International Shipping. The first line of the Frieght Forwarder main address.  """  
      self.FFAddress2:str = obj["FFAddress2"]
      """  International Shipping. The second line of the Frieght Forwarder main address.  """  
      self.FFCity:str = obj["FFCity"]
      """  Shipping, The city portion of the Frieght Forwarder main address.  """  
      self.FFState:str = obj["FFState"]
      """  International Shipping. The state or province portion of the shipment Frieght Forwarder main address.  """  
      self.FFZip:str = obj["FFZip"]
      """  International Shipping. The zip or postal code portion of the shipping Frieght Forwarder main address.  """  
      self.FFCountry:str = obj["FFCountry"]
      """  International shipping. The country of the Frieght Forwarder .  """  
      self.FFContact:str = obj["FFContact"]
      """  International Shipping. Frieght Forwarder Contact  """  
      self.FFCompName:str = obj["FFCompName"]
      """  International Shipping. Frieght Forwarder company name  """  
      self.FFPhoneNum:str = obj["FFPhoneNum"]
      """  International Shipping. Frieght Forwarder Phone number  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  Userid of user who made the last change to this record.  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  The date that the record was last changed  """  
      self.ChangeTime:int = obj["ChangeTime"]
      """  The time that the record was last change (seconds since midnight)  """  
      self.IndividualPackIDs:bool = obj["IndividualPackIDs"]
      """  Individual Pack IDs  """  
      self.FFCountryNum:int = obj["FFCountryNum"]
      """  Freight Forwarder Third address line  """  
      self.NonStdPkg:bool = obj["NonStdPkg"]
      """  Additional Handling flag  """  
      self.DeliveryConf:int = obj["DeliveryConf"]
      """   Determines the level of delivery confirmation.
1 - No Signature Required
2 - Adult Signature Required
3 - Confirmation Required
4 - Verbal Confirmation Required  """  
      self.AddlHdlgFlag:bool = obj["AddlHdlgFlag"]
      """  Non Standard Packaging  """  
      self.UPSQuantumView:bool = obj["UPSQuantumView"]
      """  UPS Quantum View  """  
      self.UPSQVShipFromName:str = obj["UPSQVShipFromName"]
      """  UPS Quantum View From Name  """  
      self.UPSQVMemo:str = obj["UPSQVMemo"]
      """  UPS Quantum View Memo  """  
      self.FFAddress3:str = obj["FFAddress3"]
      """  Freight Forwarder Country portion of the address  """  
      self.ETCAddrChg:bool = obj["ETCAddrChg"]
      """  Used to determine if an address changed because of the tax integration.  If true, the tax integration changed the address.  """  
      self.IsAlternate:bool = obj["IsAlternate"]
      """  Indicates if this is a alternate ShipTo. An alternate is a Shipto that is valid for this customer, but is defined/maintained by the "master" customer. See ShipTo.MasterCustNum/MasterShiptoNum.  """  
      self.MasterCustNum:int = obj["MasterCustNum"]
      """  Pertains to Alternate Shipto (IsAlternate). Contains the CustNum of the Shipto record that is the "Master". Changes made to the Master, are replicated to the alternates.  """  
      self.MasterShipToNum:str = obj["MasterShipToNum"]
      """  Pertains to Alternate Shipto (IsAlternate). Contains the ShipToNum of the Shipto record that is the "Master". Changes made to the Master, are replicated to the alternates.  """  
      self.DemandCheckForRev:bool = obj["DemandCheckForRev"]
      """  Check for Revision  """  
      self.DemandCheckForRevAction:str = obj["DemandCheckForRevAction"]
      """  Check for Revision Action  """  
      self.DemandCheckPartialShip:bool = obj["DemandCheckPartialShip"]
      """  Flag for checking partial Shipment for Demand Entry.  """  
      self.DemandCheckShipAction:str = obj["DemandCheckShipAction"]
      """  Check Partial Shipments Action: B =Stop  and W = Warning  """  
      self.DemandCloseRejSkd:bool = obj["DemandCloseRejSkd"]
      """  Define if at the moment of processing a demand the process should also close those rejected schedules that remain at demand entry  """  
      self.DemandPricing:str = obj["DemandPricing"]
      """  Defines if Internal Pricing or Customer Pricing will be used for checking price differences  """  
      self.PriceTolerance:int = obj["PriceTolerance"]
      """  Defines the tolerance for price difference validations  """  
      self.CheckDateCapPromise:bool = obj["CheckDateCapPromise"]
      """  If this flags is turned on then Demand CTP will automatically be executed as a part of the demand to order process.  """  
      self.CheckConfirmCapPromise:bool = obj["CheckConfirmCapPromise"]
      """  Confirm or not the Capable to Promise jobs from Demand Entry  """  
      self.CheckUpdateCapPromise:bool = obj["CheckUpdateCapPromise"]
      """  If checked, Updates the date in Demand Entry  """  
      self.DemandCapPromiseDate:str = obj["DemandCapPromiseDate"]
      """  This field will define the dates that will be validated as a part of the demand to order process. The valid values for this combo will be:  Need By (N), Ship By (S) and Both (B)  """  
      self.DemandCapPromiseAction:str = obj["DemandCapPromiseAction"]
      """  The value on this field will define the action to be taken when validating CTP. The valid values for this combo box will be: Warning (W) and Stop (S)  """  
      self.DemandCapPromiseUpdate:str = obj["DemandCapPromiseUpdate"]
      """   This field will define the dates that will be updated as a part of the demand to order process. The valid options will be:
Need By (N), Ship By (S) and Both  (B) NOTE .-In all the cases above the update of date will only be done if the CTP dates are beyond the dates on the file.  """  
      self.OTSmartString:bool = obj["OTSmartString"]
      """  When set to TRUE the smart string functionality will only be processed when the incoming demand is new. After it has been processed and saved, if a retransmission is sent the smart string values will be ignored.  """  
      self.LegalName:str = obj["LegalName"]
      """  Full Legal name  """  
      self.DemandCheckConfig:bool = obj["DemandCheckConfig"]
      """  If true then demand will be rejected when one or more demand lines are not configured properly. Applies only to Configurable parts.  """  
      self.DemandCheckCfgAction:str = obj["DemandCheckCfgAction"]
      """  Indicates the action to be taken if configuration values have not been entered for one or more demand lines.  """  
      self.WIWebShipTo:bool = obj["WIWebShipTo"]
      """  WIWebShipTo  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.AGApartment:str = obj["AGApartment"]
      """  AGApartment  """  
      self.AGExtraStreetNumber:str = obj["AGExtraStreetNumber"]
      """  AGExtraStreetNumber  """  
      self.AGFloor:str = obj["AGFloor"]
      """  AGFloor  """  
      self.AGGrossIncomeTaxID:str = obj["AGGrossIncomeTaxID"]
      """  AGGrossIncomeTaxID  """  
      self.AGLocationCode:str = obj["AGLocationCode"]
      """  AGLocationCode  """  
      self.AGNeighborhood:str = obj["AGNeighborhood"]
      """  AGNeighborhood  """  
      self.AGProvinceCode:str = obj["AGProvinceCode"]
      """  AGProvinceCode  """  
      self.AGStreet:str = obj["AGStreet"]
      """  AGStreet  """  
      self.AGStreetNumber:str = obj["AGStreetNumber"]
      """  AGStreetNumber  """  
      self.EntityUseCode:str = obj["EntityUseCode"]
      """  EntityUseCode  """  
      self.DemandCheckForRunOutPart:bool = obj["DemandCheckForRunOutPart"]
      """  Check if the part is a run out part.  """  
      self.DemandCheckForRunOutPartAction:str = obj["DemandCheckForRunOutPartAction"]
      """  Indicates what type of action to take if the Check for Run Out Part option is selected and the part is marked as a run out part.  Options are B (reject the change) or W (warning - alert that the part is marked as run out but allow the record to be accepted).  """  
      self.INExciseRegNumber:str = obj["INExciseRegNumber"]
      """  INExciseRegNumber  """  
      self.INVATNumber:str = obj["INVATNumber"]
      """  INVATNumber  """  
      self.INSTRegistration:str = obj["INSTRegistration"]
      """  INSTRegistration  """  
      self.MXCURP:str = obj["MXCURP"]
      """  MXCURP  """  
      self.MXMunicipio:str = obj["MXMunicipio"]
      """  MXMunicipio  """  
      self.MXFederalID:str = obj["MXFederalID"]
      """  MXFederalID  """  
      self.INTaxRegistrationID:str = obj["INTaxRegistrationID"]
      """  INTaxRegistrationID  """  
      self.PEUBIGEOCode:str = obj["PEUBIGEOCode"]
      """  Geographical Location Code  """  
      self.EORINumber:str = obj["EORINumber"]
      """  EORI Number  """  
      self.TaxValidationStatus:int = obj["TaxValidationStatus"]
      """  Tax ID Validation Status: Not Validated – 0, Valid – 1, Invalid – 2.  """  
      self.TaxValidationDate:str = obj["TaxValidationDate"]
      """  Tax Validation Date  """  
      self.HMRCTaxValidationLog:str = obj["HMRCTaxValidationLog"]
      """  HMRCTaxValidationLog  """  
      self.Inactive:bool = obj["Inactive"]
      """  Indicates if the record is inactive.  """  
      self.FSMRegionCode:str = obj["FSMRegionCode"]
      """  FSMRegionCode  """  
      self.FSMArea:str = obj["FSMArea"]
      """  FSMArea  """  
      self.COASegReferences:str = obj["COASegReferences"]
      """  List of fields which are referenced by COA segments.  """  
      self.ContactName:str = obj["ContactName"]
      """  Used for ContactTracker.  This is needed so the UI can relate the Contact Tracker tables together.  """  
      self.DspFormatStr:str = obj["DspFormatStr"]
      """  Display Format String  """  
      self.GlbFlag:bool = obj["GlbFlag"]
      """  Indicates if ShipTo is Global (Master or Linked)  """  
      self.GlbLink:str = obj["GlbLink"]
      """  Delimited list of GlbCompany, GlbCustNum and GlbShipto that is linking to this shipto  """  
      self.IntegrationFlag:bool = obj["IntegrationFlag"]
      """  Indicates Integration with financial package (like EuroFin)  """  
      self.IntRunChangeCountry:bool = obj["IntRunChangeCountry"]
      """  Flag used for integrations whether to run the on change country logic.  """  
      self.PeriodicityDesc:str = obj["PeriodicityDesc"]
      self.PeriodicityList:str = obj["PeriodicityList"]
      """  List of available Periodicity values  """  
      self.PrimaryShipTo:bool = obj["PrimaryShipTo"]
      """  Used to indicate if primary shipto.  Updates Customer.ShipToNum field  """  
      self.SalesTaxID:str = obj["SalesTaxID"]
      """  Sales Tax ID  """  
      self.ServiceTaxID:str = obj["ServiceTaxID"]
      """  Service Tax ID  """  
      self.TerritorySelectDescription:str = obj["TerritorySelectDescription"]
      self.TerrSelectFlag:str = obj["TerrSelectFlag"]
      """  Use this field to display/update; replaces TerritorySelect  """  
      self.AddrList:str = obj["AddrList"]
      """  Address in formatted delimited list  """  
      self.LanguageDescription:str = obj["LanguageDescription"]
      self.BitFlag:int = obj["BitFlag"]
      self.AGLocationDescription:str = obj["AGLocationDescription"]
      self.AGProvinceDescription:str = obj["AGProvinceDescription"]
      self.CountryISOCode:str = obj["CountryISOCode"]
      self.CountryEUMember:bool = obj["CountryEUMember"]
      self.CustNumName:str = obj["CustNumName"]
      self.CustNumCustID:str = obj["CustNumCustID"]
      self.CustNumBTName:str = obj["CustNumBTName"]
      self.DeliveryTypeDescription:str = obj["DeliveryTypeDescription"]
      self.MasterCustIDBTName:str = obj["MasterCustIDBTName"]
      self.MasterCustIDCustID:str = obj["MasterCustIDCustID"]
      self.MasterCustIDName:str = obj["MasterCustIDName"]
      self.SalesRepName:str = obj["SalesRepName"]
      self.ShipViaWebDesc:str = obj["ShipViaWebDesc"]
      self.ShipViaDescription:str = obj["ShipViaDescription"]
      self.TATaxAuthorityDescription:str = obj["TATaxAuthorityDescription"]
      self.TaxRegionDescription:str = obj["TaxRegionDescription"]
      self.TerritoryTerritoryDesc:str = obj["TerritoryTerritoryDesc"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ShipToTableset:
   def __init__(self, obj):
      self.ShipTo:list[Erp_Tablesets_ShipToRow] = obj["ShipTo"]
      self.ShipToAttch:list[Erp_Tablesets_ShipToAttchRow] = obj["ShipToAttch"]
      self.ShipToLabExpRate:list[Erp_Tablesets_ShipToLabExpRateRow] = obj["ShipToLabExpRate"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_UpdExtShipToTableset:
   def __init__(self, obj):
      self.ShipTo:list[Erp_Tablesets_ShipToRow] = obj["ShipTo"]
      self.ShipToAttch:list[Erp_Tablesets_ShipToAttchRow] = obj["ShipToAttch"]
      self.ShipToLabExpRate:list[Erp_Tablesets_ShipToLabExpRateRow] = obj["ShipToLabExpRate"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetByID_input:
   """ Required : 
   custNum
   shipToNum
   """  
   def __init__(self, obj):
      self.custNum:int = obj["custNum"]
      self.shipToNum:str = obj["shipToNum"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ShipToTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_ShipToTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_ShipToTableset] = obj["returnObj"]
      pass

class GetListFilterCustomer_input:
   """ Required : 
   WhereClause
   PageSize
   AbsolutePage
   """  
   def __init__(self, obj):
      self.WhereClause:str = obj["WhereClause"]
      """  Whereclause.  """  
      self.PageSize:int = obj["PageSize"]
      """  Page size.  """  
      self.AbsolutePage:int = obj["AbsolutePage"]
      """  Absolute page.  """  
      pass

class GetListFilterCustomer_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ShipToListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.MorePages:bool = obj["MorePages"]
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
      self.returnObj:list[Erp_Tablesets_ShipToListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewShipToAttch_input:
   """ Required : 
   ds
   custNum
   shipToNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ShipToTableset] = obj["ds"]
      self.custNum:int = obj["custNum"]
      self.shipToNum:str = obj["shipToNum"]
      pass

class GetNewShipToAttch_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ShipToTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewShipToLabExpRate_input:
   """ Required : 
   ds
   custNum
   shipToNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ShipToTableset] = obj["ds"]
      self.custNum:int = obj["custNum"]
      self.shipToNum:str = obj["shipToNum"]
      pass

class GetNewShipToLabExpRate_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ShipToTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewShipTo_input:
   """ Required : 
   ds
   custNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ShipToTableset] = obj["ds"]
      self.custNum:int = obj["custNum"]
      pass

class GetNewShipTo_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ShipToTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseShipTo
   whereClauseShipToAttch
   whereClauseShipToLabExpRate
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseShipTo:str = obj["whereClauseShipTo"]
      self.whereClauseShipToAttch:str = obj["whereClauseShipToAttch"]
      self.whereClauseShipToLabExpRate:str = obj["whereClauseShipToLabExpRate"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ShipToTableset] = obj["returnObj"]
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
      self.ds:list[Erp_Tablesets_UpdExtShipToTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtShipToTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ShipToTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ShipToTableset] = obj["ds"]
      pass

      """  output parameters  """  

