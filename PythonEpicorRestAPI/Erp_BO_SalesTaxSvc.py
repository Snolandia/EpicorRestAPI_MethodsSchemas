import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.SalesTaxSvc
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.SalesTaxSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.SalesTaxSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_SalesTaxes(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get SalesTaxes items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_SalesTaxes
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.SalesTaxRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.SalesTaxSvc/SalesTaxes",headers=creds) as resp:
           return await resp.json()

async def post_SalesTaxes(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_SalesTaxes
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.SalesTaxRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.SalesTaxRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SalesTaxSvc/SalesTaxes", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_SalesTaxes_Company_TaxCode(Company, TaxCode, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the SalesTax item
   Description: Calls GetByID to retrieve the SalesTax item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_SalesTax
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TaxCode: Desc: TaxCode   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.SalesTaxRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.SalesTaxSvc/SalesTaxes(" + Company + "," + TaxCode + ")",headers=creds) as resp:
           return await resp.json()

async def patch_SalesTaxes_Company_TaxCode(Company, TaxCode, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update SalesTax for the service
   Description: Calls UpdateExt to update SalesTax. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_SalesTax
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TaxCode: Desc: TaxCode   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.SalesTaxRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.SalesTaxSvc/SalesTaxes(" + Company + "," + TaxCode + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_SalesTaxes_Company_TaxCode(Company, TaxCode, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete SalesTax item
   Description: Call UpdateExt to delete SalesTax item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_SalesTax
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TaxCode: Desc: TaxCode   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.SalesTaxSvc/SalesTaxes(" + Company + "," + TaxCode + ")",headers=creds) as resp:
           return await resp.json()

async def get_SalesTaxes_Company_TaxCode_LangDescs(Company, TaxCode, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get LangDescs items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_LangDescs1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TaxCode: Desc: TaxCode   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.LangDescRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.SalesTaxSvc/SalesTaxes(" + Company + "," + TaxCode + ")/LangDescs",headers=creds) as resp:
           return await resp.json()

async def get_SalesTaxes_Company_TaxCode_LangDescs_Company_TableName_Key1_Key2_Key3_LangNameID(Company, TaxCode, TableName, Key1, Key2, Key3, LangNameID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the LangDesc item
   Description: Calls GetByID to retrieve the LangDesc item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_LangDesc1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TaxCode: Desc: TaxCode   Required: True   Allow empty value : True
      :param TableName: Desc: TableName   Required: True   Allow empty value : True
      :param Key1: Desc: Key1   Required: True   Allow empty value : True
      :param Key2: Desc: Key2   Required: True   Allow empty value : True
      :param Key3: Desc: Key3   Required: True   Allow empty value : True
      :param LangNameID: Desc: LangNameID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.LangDescRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.SalesTaxSvc/SalesTaxes(" + Company + "," + TaxCode + ")/LangDescs(" + Company + "," + TableName + "," + Key1 + "," + Key2 + "," + Key3 + "," + LangNameID + ")",headers=creds) as resp:
           return await resp.json()

async def get_SalesTaxes_Company_TaxCode_SalesTRCs(Company, TaxCode, select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get SalesTRCs items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_SalesTRCs1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TaxCode: Desc: TaxCode   Required: True   Allow empty value : True
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.SalesTRCRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.SalesTaxSvc/SalesTaxes(" + Company + "," + TaxCode + ")/SalesTRCs",headers=creds) as resp:
           return await resp.json()

async def get_SalesTaxes_Company_TaxCode_SalesTRCs_Company_TaxCode_RateCode(Company, TaxCode, RateCode, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the SalesTRC item
   Description: Calls GetByID to retrieve the SalesTRC item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_SalesTRC1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TaxCode: Desc: TaxCode   Required: True   Allow empty value : True
      :param RateCode: Desc: RateCode   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.SalesTRCRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.SalesTaxSvc/SalesTaxes(" + Company + "," + TaxCode + ")/SalesTRCs(" + Company + "," + TaxCode + "," + RateCode + ")",headers=creds) as resp:
           return await resp.json()

async def get_LangDescs(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get LangDescs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_LangDescs
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.LangDescRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.SalesTaxSvc/LangDescs",headers=creds) as resp:
           return await resp.json()

async def post_LangDescs(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_LangDescs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.LangDescRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.LangDescRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SalesTaxSvc/LangDescs", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_LangDescs_Company_TableName_Key1_Key2_Key3_LangNameID(Company, TableName, Key1, Key2, Key3, LangNameID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the LangDesc item
   Description: Calls GetByID to retrieve the LangDesc item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_LangDesc
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TableName: Desc: TableName   Required: True   Allow empty value : True
      :param Key1: Desc: Key1   Required: True   Allow empty value : True
      :param Key2: Desc: Key2   Required: True   Allow empty value : True
      :param Key3: Desc: Key3   Required: True   Allow empty value : True
      :param LangNameID: Desc: LangNameID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.LangDescRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.SalesTaxSvc/LangDescs(" + Company + "," + TableName + "," + Key1 + "," + Key2 + "," + Key3 + "," + LangNameID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_LangDescs_Company_TableName_Key1_Key2_Key3_LangNameID(Company, TableName, Key1, Key2, Key3, LangNameID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update LangDesc for the service
   Description: Calls UpdateExt to update LangDesc. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_LangDesc
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TableName: Desc: TableName   Required: True   Allow empty value : True
      :param Key1: Desc: Key1   Required: True   Allow empty value : True
      :param Key2: Desc: Key2   Required: True   Allow empty value : True
      :param Key3: Desc: Key3   Required: True   Allow empty value : True
      :param LangNameID: Desc: LangNameID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.LangDescRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.SalesTaxSvc/LangDescs(" + Company + "," + TableName + "," + Key1 + "," + Key2 + "," + Key3 + "," + LangNameID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_LangDescs_Company_TableName_Key1_Key2_Key3_LangNameID(Company, TableName, Key1, Key2, Key3, LangNameID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete LangDesc item
   Description: Call UpdateExt to delete LangDesc item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_LangDesc
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TableName: Desc: TableName   Required: True   Allow empty value : True
      :param Key1: Desc: Key1   Required: True   Allow empty value : True
      :param Key2: Desc: Key2   Required: True   Allow empty value : True
      :param Key3: Desc: Key3   Required: True   Allow empty value : True
      :param LangNameID: Desc: LangNameID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.SalesTaxSvc/LangDescs(" + Company + "," + TableName + "," + Key1 + "," + Key2 + "," + Key3 + "," + LangNameID + ")",headers=creds) as resp:
           return await resp.json()

async def get_SalesTRCs(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get SalesTRCs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_SalesTRCs
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.SalesTRCRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.SalesTaxSvc/SalesTRCs",headers=creds) as resp:
           return await resp.json()

async def post_SalesTRCs(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_SalesTRCs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.SalesTRCRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.SalesTRCRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SalesTaxSvc/SalesTRCs", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_SalesTRCs_Company_TaxCode_RateCode(Company, TaxCode, RateCode, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the SalesTRC item
   Description: Calls GetByID to retrieve the SalesTRC item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_SalesTRC
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TaxCode: Desc: TaxCode   Required: True   Allow empty value : True
      :param RateCode: Desc: RateCode   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.SalesTRCRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.SalesTaxSvc/SalesTRCs(" + Company + "," + TaxCode + "," + RateCode + ")",headers=creds) as resp:
           return await resp.json()

async def patch_SalesTRCs_Company_TaxCode_RateCode(Company, TaxCode, RateCode, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update SalesTRC for the service
   Description: Calls UpdateExt to update SalesTRC. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_SalesTRC
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TaxCode: Desc: TaxCode   Required: True   Allow empty value : True
      :param RateCode: Desc: RateCode   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.SalesTRCRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.SalesTaxSvc/SalesTRCs(" + Company + "," + TaxCode + "," + RateCode + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_SalesTRCs_Company_TaxCode_RateCode(Company, TaxCode, RateCode, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete SalesTRC item
   Description: Call UpdateExt to delete SalesTRC item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_SalesTRC
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TaxCode: Desc: TaxCode   Required: True   Allow empty value : True
      :param RateCode: Desc: RateCode   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.SalesTaxSvc/SalesTRCs(" + Company + "," + TaxCode + "," + RateCode + ")",headers=creds) as resp:
           return await resp.json()

async def get_SalesTRCs_Company_TaxCode_RateCode_EntityGLCs(Company, TaxCode, RateCode, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get EntityGLCs items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_EntityGLCs1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TaxCode: Desc: TaxCode   Required: True   Allow empty value : True
      :param RateCode: Desc: RateCode   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.EntityGLCRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.SalesTaxSvc/SalesTRCs(" + Company + "," + TaxCode + "," + RateCode + ")/EntityGLCs",headers=creds) as resp:
           return await resp.json()

async def get_SalesTRCs_Company_TaxCode_RateCode_EntityGLCs_Company_RelatedToFile_Key1_Key2_Key3_Key4_Key5_Key6_GLControlType(Company, TaxCode, RateCode, RelatedToFile, Key1, Key2, Key3, Key4, Key5, Key6, GLControlType, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the EntityGLC item
   Description: Calls GetByID to retrieve the EntityGLC item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_EntityGLC1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TaxCode: Desc: TaxCode   Required: True   Allow empty value : True
      :param RateCode: Desc: RateCode   Required: True   Allow empty value : True
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
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.EntityGLCRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.SalesTaxSvc/SalesTRCs(" + Company + "," + TaxCode + "," + RateCode + ")/EntityGLCs(" + Company + "," + RelatedToFile + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + Key6 + "," + GLControlType + ")",headers=creds) as resp:
           return await resp.json()

async def get_SalesTRCs_Company_TaxCode_RateCode_SalesTxcs(Company, TaxCode, RateCode, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get SalesTxcs items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_SalesTxcs1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TaxCode: Desc: TaxCode   Required: True   Allow empty value : True
      :param RateCode: Desc: RateCode   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.SalesTxcRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.SalesTaxSvc/SalesTRCs(" + Company + "," + TaxCode + "," + RateCode + ")/SalesTxcs",headers=creds) as resp:
           return await resp.json()

async def get_SalesTRCs_Company_TaxCode_RateCode_SalesTxcs_Company_TaxCode_RateCode_TaxCatID(Company, TaxCode, RateCode, TaxCatID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the SalesTxc item
   Description: Calls GetByID to retrieve the SalesTxc item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_SalesTxc1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TaxCode: Desc: TaxCode   Required: True   Allow empty value : True
      :param RateCode: Desc: RateCode   Required: True   Allow empty value : True
      :param TaxCatID: Desc: TaxCatID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.SalesTxcRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.SalesTaxSvc/SalesTRCs(" + Company + "," + TaxCode + "," + RateCode + ")/SalesTxcs(" + Company + "," + TaxCode + "," + RateCode + "," + TaxCatID + ")",headers=creds) as resp:
           return await resp.json()

async def get_SalesTRCs_Company_TaxCode_RateCode_TaxBoxes(Company, TaxCode, RateCode, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get TaxBoxes items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_TaxBoxes1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TaxCode: Desc: TaxCode   Required: True   Allow empty value : True
      :param RateCode: Desc: RateCode   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.TaxBoxRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.SalesTaxSvc/SalesTRCs(" + Company + "," + TaxCode + "," + RateCode + ")/TaxBoxes",headers=creds) as resp:
           return await resp.json()

async def get_SalesTRCs_Company_TaxCode_RateCode_TaxBoxes_Company_TaxCode_RateCode_BoxCode_SourceModule_AmountType_ECAcquisitionSeq(Company, TaxCode, RateCode, BoxCode, SourceModule, AmountType, ECAcquisitionSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the TaxBox item
   Description: Calls GetByID to retrieve the TaxBox item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_TaxBox1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TaxCode: Desc: TaxCode   Required: True   Allow empty value : True
      :param RateCode: Desc: RateCode   Required: True   Allow empty value : True
      :param BoxCode: Desc: BoxCode   Required: True   Allow empty value : True
      :param SourceModule: Desc: SourceModule   Required: True   Allow empty value : True
      :param AmountType: Desc: AmountType   Required: True   Allow empty value : True
      :param ECAcquisitionSeq: Desc: ECAcquisitionSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.TaxBoxRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.SalesTaxSvc/SalesTRCs(" + Company + "," + TaxCode + "," + RateCode + ")/TaxBoxes(" + Company + "," + TaxCode + "," + RateCode + "," + BoxCode + "," + SourceModule + "," + AmountType + "," + ECAcquisitionSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_SalesTRCs_Company_TaxCode_RateCode_TaxRates(Company, TaxCode, RateCode, select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get TaxRates items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_TaxRates1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TaxCode: Desc: TaxCode   Required: True   Allow empty value : True
      :param RateCode: Desc: RateCode   Required: True   Allow empty value : True
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.TaxRateRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.SalesTaxSvc/SalesTRCs(" + Company + "," + TaxCode + "," + RateCode + ")/TaxRates",headers=creds) as resp:
           return await resp.json()

async def get_SalesTRCs_Company_TaxCode_RateCode_TaxRates_Company_TaxCode_RateCode_EffectiveFrom(Company, TaxCode, RateCode, EffectiveFrom, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the TaxRate item
   Description: Calls GetByID to retrieve the TaxRate item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_TaxRate1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TaxCode: Desc: TaxCode   Required: True   Allow empty value : True
      :param RateCode: Desc: RateCode   Required: True   Allow empty value : True
      :param EffectiveFrom: Desc: EffectiveFrom   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.TaxRateRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.SalesTaxSvc/SalesTRCs(" + Company + "," + TaxCode + "," + RateCode + ")/TaxRates(" + Company + "," + TaxCode + "," + RateCode + "," + EffectiveFrom + ")",headers=creds) as resp:
           return await resp.json()

async def get_SalesTRCs_Company_TaxCode_RateCode_PLSAFTCodes(Company, TaxCode, RateCode, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get PLSAFTCodes items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_PLSAFTCodes1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TaxCode: Desc: TaxCode   Required: True   Allow empty value : True
      :param RateCode: Desc: RateCode   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PLSAFTCodeRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.SalesTaxSvc/SalesTRCs(" + Company + "," + TaxCode + "," + RateCode + ")/PLSAFTCodes",headers=creds) as resp:
           return await resp.json()

async def get_SalesTRCs_Company_TaxCode_RateCode_PLSAFTCodes_Company_RateCode_TaxCode_SAFTCode(Company, TaxCode, RateCode, SAFTCode, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PLSAFTCode item
   Description: Calls GetByID to retrieve the PLSAFTCode item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PLSAFTCode1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TaxCode: Desc: TaxCode   Required: True   Allow empty value : True
      :param RateCode: Desc: RateCode   Required: True   Allow empty value : True
      :param SAFTCode: Desc: SAFTCode   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PLSAFTCodeRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.SalesTaxSvc/SalesTRCs(" + Company + "," + TaxCode + "," + RateCode + ")/PLSAFTCodes(" + Company + "," + RateCode + "," + TaxCode + "," + SAFTCode + ")",headers=creds) as resp:
           return await resp.json()

async def get_EntityGLCs(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get EntityGLCs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_EntityGLCs
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.EntityGLCRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.SalesTaxSvc/EntityGLCs",headers=creds) as resp:
           return await resp.json()

async def post_EntityGLCs(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_EntityGLCs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.EntityGLCRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.EntityGLCRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SalesTaxSvc/EntityGLCs", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_EntityGLCs_Company_RelatedToFile_Key1_Key2_Key3_Key4_Key5_Key6_GLControlType(Company, RelatedToFile, Key1, Key2, Key3, Key4, Key5, Key6, GLControlType, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the EntityGLC item
   Description: Calls GetByID to retrieve the EntityGLC item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_EntityGLC
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
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.EntityGLCRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.SalesTaxSvc/EntityGLCs(" + Company + "," + RelatedToFile + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + Key6 + "," + GLControlType + ")",headers=creds) as resp:
           return await resp.json()

async def patch_EntityGLCs_Company_RelatedToFile_Key1_Key2_Key3_Key4_Key5_Key6_GLControlType(Company, RelatedToFile, Key1, Key2, Key3, Key4, Key5, Key6, GLControlType, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update EntityGLC for the service
   Description: Calls UpdateExt to update EntityGLC. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_EntityGLC
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
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.EntityGLCRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.SalesTaxSvc/EntityGLCs(" + Company + "," + RelatedToFile + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + Key6 + "," + GLControlType + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_EntityGLCs_Company_RelatedToFile_Key1_Key2_Key3_Key4_Key5_Key6_GLControlType(Company, RelatedToFile, Key1, Key2, Key3, Key4, Key5, Key6, GLControlType, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete EntityGLC item
   Description: Call UpdateExt to delete EntityGLC item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_EntityGLC
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.SalesTaxSvc/EntityGLCs(" + Company + "," + RelatedToFile + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + Key6 + "," + GLControlType + ")",headers=creds) as resp:
           return await resp.json()

async def get_SalesTxcs(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get SalesTxcs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_SalesTxcs
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.SalesTxcRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.SalesTaxSvc/SalesTxcs",headers=creds) as resp:
           return await resp.json()

async def post_SalesTxcs(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_SalesTxcs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.SalesTxcRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.SalesTxcRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SalesTaxSvc/SalesTxcs", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_SalesTxcs_Company_TaxCode_RateCode_TaxCatID(Company, TaxCode, RateCode, TaxCatID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the SalesTxc item
   Description: Calls GetByID to retrieve the SalesTxc item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_SalesTxc
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TaxCode: Desc: TaxCode   Required: True   Allow empty value : True
      :param RateCode: Desc: RateCode   Required: True   Allow empty value : True
      :param TaxCatID: Desc: TaxCatID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.SalesTxcRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.SalesTaxSvc/SalesTxcs(" + Company + "," + TaxCode + "," + RateCode + "," + TaxCatID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_SalesTxcs_Company_TaxCode_RateCode_TaxCatID(Company, TaxCode, RateCode, TaxCatID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update SalesTxc for the service
   Description: Calls UpdateExt to update SalesTxc. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_SalesTxc
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TaxCode: Desc: TaxCode   Required: True   Allow empty value : True
      :param RateCode: Desc: RateCode   Required: True   Allow empty value : True
      :param TaxCatID: Desc: TaxCatID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.SalesTxcRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.SalesTaxSvc/SalesTxcs(" + Company + "," + TaxCode + "," + RateCode + "," + TaxCatID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_SalesTxcs_Company_TaxCode_RateCode_TaxCatID(Company, TaxCode, RateCode, TaxCatID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete SalesTxc item
   Description: Call UpdateExt to delete SalesTxc item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_SalesTxc
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TaxCode: Desc: TaxCode   Required: True   Allow empty value : True
      :param RateCode: Desc: RateCode   Required: True   Allow empty value : True
      :param TaxCatID: Desc: TaxCatID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.SalesTaxSvc/SalesTxcs(" + Company + "," + TaxCode + "," + RateCode + "," + TaxCatID + ")",headers=creds) as resp:
           return await resp.json()

async def get_TaxBoxes(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get TaxBoxes items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_TaxBoxes
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.TaxBoxRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.SalesTaxSvc/TaxBoxes",headers=creds) as resp:
           return await resp.json()

async def post_TaxBoxes(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_TaxBoxes
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.TaxBoxRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.TaxBoxRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SalesTaxSvc/TaxBoxes", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_TaxBoxes_Company_TaxCode_RateCode_BoxCode_SourceModule_AmountType_ECAcquisitionSeq(Company, TaxCode, RateCode, BoxCode, SourceModule, AmountType, ECAcquisitionSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the TaxBox item
   Description: Calls GetByID to retrieve the TaxBox item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_TaxBox
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TaxCode: Desc: TaxCode   Required: True   Allow empty value : True
      :param RateCode: Desc: RateCode   Required: True   Allow empty value : True
      :param BoxCode: Desc: BoxCode   Required: True   Allow empty value : True
      :param SourceModule: Desc: SourceModule   Required: True   Allow empty value : True
      :param AmountType: Desc: AmountType   Required: True   Allow empty value : True
      :param ECAcquisitionSeq: Desc: ECAcquisitionSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.TaxBoxRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.SalesTaxSvc/TaxBoxes(" + Company + "," + TaxCode + "," + RateCode + "," + BoxCode + "," + SourceModule + "," + AmountType + "," + ECAcquisitionSeq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_TaxBoxes_Company_TaxCode_RateCode_BoxCode_SourceModule_AmountType_ECAcquisitionSeq(Company, TaxCode, RateCode, BoxCode, SourceModule, AmountType, ECAcquisitionSeq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update TaxBox for the service
   Description: Calls UpdateExt to update TaxBox. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_TaxBox
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TaxCode: Desc: TaxCode   Required: True   Allow empty value : True
      :param RateCode: Desc: RateCode   Required: True   Allow empty value : True
      :param BoxCode: Desc: BoxCode   Required: True   Allow empty value : True
      :param SourceModule: Desc: SourceModule   Required: True   Allow empty value : True
      :param AmountType: Desc: AmountType   Required: True   Allow empty value : True
      :param ECAcquisitionSeq: Desc: ECAcquisitionSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.TaxBoxRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.SalesTaxSvc/TaxBoxes(" + Company + "," + TaxCode + "," + RateCode + "," + BoxCode + "," + SourceModule + "," + AmountType + "," + ECAcquisitionSeq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_TaxBoxes_Company_TaxCode_RateCode_BoxCode_SourceModule_AmountType_ECAcquisitionSeq(Company, TaxCode, RateCode, BoxCode, SourceModule, AmountType, ECAcquisitionSeq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete TaxBox item
   Description: Call UpdateExt to delete TaxBox item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_TaxBox
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TaxCode: Desc: TaxCode   Required: True   Allow empty value : True
      :param RateCode: Desc: RateCode   Required: True   Allow empty value : True
      :param BoxCode: Desc: BoxCode   Required: True   Allow empty value : True
      :param SourceModule: Desc: SourceModule   Required: True   Allow empty value : True
      :param AmountType: Desc: AmountType   Required: True   Allow empty value : True
      :param ECAcquisitionSeq: Desc: ECAcquisitionSeq   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.SalesTaxSvc/TaxBoxes(" + Company + "," + TaxCode + "," + RateCode + "," + BoxCode + "," + SourceModule + "," + AmountType + "," + ECAcquisitionSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_TaxRates(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get TaxRates items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_TaxRates
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.TaxRateRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.SalesTaxSvc/TaxRates",headers=creds) as resp:
           return await resp.json()

async def post_TaxRates(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_TaxRates
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.TaxRateRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.TaxRateRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SalesTaxSvc/TaxRates", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_TaxRates_Company_TaxCode_RateCode_EffectiveFrom(Company, TaxCode, RateCode, EffectiveFrom, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the TaxRate item
   Description: Calls GetByID to retrieve the TaxRate item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_TaxRate
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TaxCode: Desc: TaxCode   Required: True   Allow empty value : True
      :param RateCode: Desc: RateCode   Required: True   Allow empty value : True
      :param EffectiveFrom: Desc: EffectiveFrom   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.TaxRateRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.SalesTaxSvc/TaxRates(" + Company + "," + TaxCode + "," + RateCode + "," + EffectiveFrom + ")",headers=creds) as resp:
           return await resp.json()

async def patch_TaxRates_Company_TaxCode_RateCode_EffectiveFrom(Company, TaxCode, RateCode, EffectiveFrom, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update TaxRate for the service
   Description: Calls UpdateExt to update TaxRate. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_TaxRate
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TaxCode: Desc: TaxCode   Required: True   Allow empty value : True
      :param RateCode: Desc: RateCode   Required: True   Allow empty value : True
      :param EffectiveFrom: Desc: EffectiveFrom   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.TaxRateRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.SalesTaxSvc/TaxRates(" + Company + "," + TaxCode + "," + RateCode + "," + EffectiveFrom + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_TaxRates_Company_TaxCode_RateCode_EffectiveFrom(Company, TaxCode, RateCode, EffectiveFrom, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete TaxRate item
   Description: Call UpdateExt to delete TaxRate item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_TaxRate
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TaxCode: Desc: TaxCode   Required: True   Allow empty value : True
      :param RateCode: Desc: RateCode   Required: True   Allow empty value : True
      :param EffectiveFrom: Desc: EffectiveFrom   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.SalesTaxSvc/TaxRates(" + Company + "," + TaxCode + "," + RateCode + "," + EffectiveFrom + ")",headers=creds) as resp:
           return await resp.json()

async def get_TaxRates_Company_TaxCode_RateCode_EffectiveFrom_EffRateEntityGLCs(Company, TaxCode, RateCode, EffectiveFrom, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get EffRateEntityGLCs items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_EffRateEntityGLCs1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TaxCode: Desc: TaxCode   Required: True   Allow empty value : True
      :param RateCode: Desc: RateCode   Required: True   Allow empty value : True
      :param EffectiveFrom: Desc: EffectiveFrom   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.EffRateEntityGLCRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.SalesTaxSvc/TaxRates(" + Company + "," + TaxCode + "," + RateCode + "," + EffectiveFrom + ")/EffRateEntityGLCs",headers=creds) as resp:
           return await resp.json()

async def get_TaxRates_Company_TaxCode_RateCode_EffectiveFrom_EffRateEntityGLCs_Company_RelatedToFile_Key1_Key2_Key3_Key4_Key5_Key6_GLControlType(Company, TaxCode, RateCode, EffectiveFrom, RelatedToFile, Key1, Key2, Key3, Key4, Key5, Key6, GLControlType, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the EffRateEntityGLC item
   Description: Calls GetByID to retrieve the EffRateEntityGLC item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_EffRateEntityGLC1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TaxCode: Desc: TaxCode   Required: True   Allow empty value : True
      :param RateCode: Desc: RateCode   Required: True   Allow empty value : True
      :param EffectiveFrom: Desc: EffectiveFrom   Required: True   Allow empty value : True
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
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.EffRateEntityGLCRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.SalesTaxSvc/TaxRates(" + Company + "," + TaxCode + "," + RateCode + "," + EffectiveFrom + ")/EffRateEntityGLCs(" + Company + "," + RelatedToFile + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + Key6 + "," + GLControlType + ")",headers=creds) as resp:
           return await resp.json()

async def get_TaxRates_Company_TaxCode_RateCode_EffectiveFrom_TaxBoxEffRates(Company, TaxCode, RateCode, EffectiveFrom, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get TaxBoxEffRates items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_TaxBoxEffRates1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TaxCode: Desc: TaxCode   Required: True   Allow empty value : True
      :param RateCode: Desc: RateCode   Required: True   Allow empty value : True
      :param EffectiveFrom: Desc: EffectiveFrom   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.TaxBoxEffRateRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.SalesTaxSvc/TaxRates(" + Company + "," + TaxCode + "," + RateCode + "," + EffectiveFrom + ")/TaxBoxEffRates",headers=creds) as resp:
           return await resp.json()

async def get_TaxRates_Company_TaxCode_RateCode_EffectiveFrom_TaxBoxEffRates_Company_TaxCode_RateCode_BoxCode_SourceModule_AmountType_ECAcquisitionSeq_EffectiveFrom(Company, TaxCode, RateCode, EffectiveFrom, BoxCode, SourceModule, AmountType, ECAcquisitionSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the TaxBoxEffRate item
   Description: Calls GetByID to retrieve the TaxBoxEffRate item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_TaxBoxEffRate1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TaxCode: Desc: TaxCode   Required: True   Allow empty value : True
      :param RateCode: Desc: RateCode   Required: True   Allow empty value : True
      :param EffectiveFrom: Desc: EffectiveFrom   Required: True   Allow empty value : True
      :param BoxCode: Desc: BoxCode   Required: True   Allow empty value : True
      :param SourceModule: Desc: SourceModule   Required: True   Allow empty value : True
      :param AmountType: Desc: AmountType   Required: True   Allow empty value : True
      :param ECAcquisitionSeq: Desc: ECAcquisitionSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.TaxBoxEffRateRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.SalesTaxSvc/TaxRates(" + Company + "," + TaxCode + "," + RateCode + "," + EffectiveFrom + ")/TaxBoxEffRates(" + Company + "," + TaxCode + "," + RateCode + "," + BoxCode + "," + SourceModule + "," + AmountType + "," + ECAcquisitionSeq + "," + EffectiveFrom + ")",headers=creds) as resp:
           return await resp.json()

async def get_TaxRates_Company_TaxCode_RateCode_EffectiveFrom_TaxGRates(Company, TaxCode, RateCode, EffectiveFrom, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get TaxGRates items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_TaxGRates1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TaxCode: Desc: TaxCode   Required: True   Allow empty value : True
      :param RateCode: Desc: RateCode   Required: True   Allow empty value : True
      :param EffectiveFrom: Desc: EffectiveFrom   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.TaxGRateRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.SalesTaxSvc/TaxRates(" + Company + "," + TaxCode + "," + RateCode + "," + EffectiveFrom + ")/TaxGRates",headers=creds) as resp:
           return await resp.json()

async def get_TaxRates_Company_TaxCode_RateCode_EffectiveFrom_TaxGRates_Company_TaxCode_RateCode_EffectiveFrom_FromAmount(Company, TaxCode, RateCode, EffectiveFrom, FromAmount, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the TaxGRate item
   Description: Calls GetByID to retrieve the TaxGRate item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_TaxGRate1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TaxCode: Desc: TaxCode   Required: True   Allow empty value : True
      :param RateCode: Desc: RateCode   Required: True   Allow empty value : True
      :param EffectiveFrom: Desc: EffectiveFrom   Required: True   Allow empty value : True
      :param FromAmount: Desc: FromAmount   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.TaxGRateRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.SalesTaxSvc/TaxRates(" + Company + "," + TaxCode + "," + RateCode + "," + EffectiveFrom + ")/TaxGRates(" + Company + "," + TaxCode + "," + RateCode + "," + EffectiveFrom + "," + FromAmount + ")",headers=creds) as resp:
           return await resp.json()

async def get_EffRateEntityGLCs(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get EffRateEntityGLCs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_EffRateEntityGLCs
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.EffRateEntityGLCRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.SalesTaxSvc/EffRateEntityGLCs",headers=creds) as resp:
           return await resp.json()

async def post_EffRateEntityGLCs(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_EffRateEntityGLCs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.EffRateEntityGLCRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.EffRateEntityGLCRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SalesTaxSvc/EffRateEntityGLCs", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_EffRateEntityGLCs_Company_RelatedToFile_Key1_Key2_Key3_Key4_Key5_Key6_GLControlType(Company, RelatedToFile, Key1, Key2, Key3, Key4, Key5, Key6, GLControlType, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the EffRateEntityGLC item
   Description: Calls GetByID to retrieve the EffRateEntityGLC item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_EffRateEntityGLC
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
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.EffRateEntityGLCRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.SalesTaxSvc/EffRateEntityGLCs(" + Company + "," + RelatedToFile + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + Key6 + "," + GLControlType + ")",headers=creds) as resp:
           return await resp.json()

async def patch_EffRateEntityGLCs_Company_RelatedToFile_Key1_Key2_Key3_Key4_Key5_Key6_GLControlType(Company, RelatedToFile, Key1, Key2, Key3, Key4, Key5, Key6, GLControlType, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update EffRateEntityGLC for the service
   Description: Calls UpdateExt to update EffRateEntityGLC. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_EffRateEntityGLC
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
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.EffRateEntityGLCRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.SalesTaxSvc/EffRateEntityGLCs(" + Company + "," + RelatedToFile + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + Key6 + "," + GLControlType + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_EffRateEntityGLCs_Company_RelatedToFile_Key1_Key2_Key3_Key4_Key5_Key6_GLControlType(Company, RelatedToFile, Key1, Key2, Key3, Key4, Key5, Key6, GLControlType, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete EffRateEntityGLC item
   Description: Call UpdateExt to delete EffRateEntityGLC item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_EffRateEntityGLC
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.SalesTaxSvc/EffRateEntityGLCs(" + Company + "," + RelatedToFile + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + Key6 + "," + GLControlType + ")",headers=creds) as resp:
           return await resp.json()

async def get_TaxBoxEffRates(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get TaxBoxEffRates items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_TaxBoxEffRates
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.TaxBoxEffRateRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.SalesTaxSvc/TaxBoxEffRates",headers=creds) as resp:
           return await resp.json()

async def post_TaxBoxEffRates(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_TaxBoxEffRates
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.TaxBoxEffRateRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.TaxBoxEffRateRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SalesTaxSvc/TaxBoxEffRates", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_TaxBoxEffRates_Company_TaxCode_RateCode_BoxCode_SourceModule_AmountType_ECAcquisitionSeq_EffectiveFrom(Company, TaxCode, RateCode, BoxCode, SourceModule, AmountType, ECAcquisitionSeq, EffectiveFrom, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the TaxBoxEffRate item
   Description: Calls GetByID to retrieve the TaxBoxEffRate item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_TaxBoxEffRate
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TaxCode: Desc: TaxCode   Required: True   Allow empty value : True
      :param RateCode: Desc: RateCode   Required: True   Allow empty value : True
      :param BoxCode: Desc: BoxCode   Required: True   Allow empty value : True
      :param SourceModule: Desc: SourceModule   Required: True   Allow empty value : True
      :param AmountType: Desc: AmountType   Required: True   Allow empty value : True
      :param ECAcquisitionSeq: Desc: ECAcquisitionSeq   Required: True
      :param EffectiveFrom: Desc: EffectiveFrom   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.TaxBoxEffRateRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.SalesTaxSvc/TaxBoxEffRates(" + Company + "," + TaxCode + "," + RateCode + "," + BoxCode + "," + SourceModule + "," + AmountType + "," + ECAcquisitionSeq + "," + EffectiveFrom + ")",headers=creds) as resp:
           return await resp.json()

async def patch_TaxBoxEffRates_Company_TaxCode_RateCode_BoxCode_SourceModule_AmountType_ECAcquisitionSeq_EffectiveFrom(Company, TaxCode, RateCode, BoxCode, SourceModule, AmountType, ECAcquisitionSeq, EffectiveFrom, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update TaxBoxEffRate for the service
   Description: Calls UpdateExt to update TaxBoxEffRate. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_TaxBoxEffRate
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TaxCode: Desc: TaxCode   Required: True   Allow empty value : True
      :param RateCode: Desc: RateCode   Required: True   Allow empty value : True
      :param BoxCode: Desc: BoxCode   Required: True   Allow empty value : True
      :param SourceModule: Desc: SourceModule   Required: True   Allow empty value : True
      :param AmountType: Desc: AmountType   Required: True   Allow empty value : True
      :param ECAcquisitionSeq: Desc: ECAcquisitionSeq   Required: True
      :param EffectiveFrom: Desc: EffectiveFrom   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.TaxBoxEffRateRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.SalesTaxSvc/TaxBoxEffRates(" + Company + "," + TaxCode + "," + RateCode + "," + BoxCode + "," + SourceModule + "," + AmountType + "," + ECAcquisitionSeq + "," + EffectiveFrom + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_TaxBoxEffRates_Company_TaxCode_RateCode_BoxCode_SourceModule_AmountType_ECAcquisitionSeq_EffectiveFrom(Company, TaxCode, RateCode, BoxCode, SourceModule, AmountType, ECAcquisitionSeq, EffectiveFrom, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete TaxBoxEffRate item
   Description: Call UpdateExt to delete TaxBoxEffRate item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_TaxBoxEffRate
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TaxCode: Desc: TaxCode   Required: True   Allow empty value : True
      :param RateCode: Desc: RateCode   Required: True   Allow empty value : True
      :param BoxCode: Desc: BoxCode   Required: True   Allow empty value : True
      :param SourceModule: Desc: SourceModule   Required: True   Allow empty value : True
      :param AmountType: Desc: AmountType   Required: True   Allow empty value : True
      :param ECAcquisitionSeq: Desc: ECAcquisitionSeq   Required: True
      :param EffectiveFrom: Desc: EffectiveFrom   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.SalesTaxSvc/TaxBoxEffRates(" + Company + "," + TaxCode + "," + RateCode + "," + BoxCode + "," + SourceModule + "," + AmountType + "," + ECAcquisitionSeq + "," + EffectiveFrom + ")",headers=creds) as resp:
           return await resp.json()

async def get_TaxGRates(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get TaxGRates items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_TaxGRates
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.TaxGRateRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.SalesTaxSvc/TaxGRates",headers=creds) as resp:
           return await resp.json()

async def post_TaxGRates(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_TaxGRates
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.TaxGRateRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.TaxGRateRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SalesTaxSvc/TaxGRates", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_TaxGRates_Company_TaxCode_RateCode_EffectiveFrom_FromAmount(Company, TaxCode, RateCode, EffectiveFrom, FromAmount, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the TaxGRate item
   Description: Calls GetByID to retrieve the TaxGRate item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_TaxGRate
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TaxCode: Desc: TaxCode   Required: True   Allow empty value : True
      :param RateCode: Desc: RateCode   Required: True   Allow empty value : True
      :param EffectiveFrom: Desc: EffectiveFrom   Required: True   Allow empty value : True
      :param FromAmount: Desc: FromAmount   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.TaxGRateRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.SalesTaxSvc/TaxGRates(" + Company + "," + TaxCode + "," + RateCode + "," + EffectiveFrom + "," + FromAmount + ")",headers=creds) as resp:
           return await resp.json()

async def patch_TaxGRates_Company_TaxCode_RateCode_EffectiveFrom_FromAmount(Company, TaxCode, RateCode, EffectiveFrom, FromAmount, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update TaxGRate for the service
   Description: Calls UpdateExt to update TaxGRate. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_TaxGRate
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TaxCode: Desc: TaxCode   Required: True   Allow empty value : True
      :param RateCode: Desc: RateCode   Required: True   Allow empty value : True
      :param EffectiveFrom: Desc: EffectiveFrom   Required: True   Allow empty value : True
      :param FromAmount: Desc: FromAmount   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.TaxGRateRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.SalesTaxSvc/TaxGRates(" + Company + "," + TaxCode + "," + RateCode + "," + EffectiveFrom + "," + FromAmount + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_TaxGRates_Company_TaxCode_RateCode_EffectiveFrom_FromAmount(Company, TaxCode, RateCode, EffectiveFrom, FromAmount, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete TaxGRate item
   Description: Call UpdateExt to delete TaxGRate item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_TaxGRate
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TaxCode: Desc: TaxCode   Required: True   Allow empty value : True
      :param RateCode: Desc: RateCode   Required: True   Allow empty value : True
      :param EffectiveFrom: Desc: EffectiveFrom   Required: True   Allow empty value : True
      :param FromAmount: Desc: FromAmount   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.SalesTaxSvc/TaxGRates(" + Company + "," + TaxCode + "," + RateCode + "," + EffectiveFrom + "," + FromAmount + ")",headers=creds) as resp:
           return await resp.json()

async def get_PLSAFTCodes(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get PLSAFTCodes items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PLSAFTCodes
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PLSAFTCodeRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.SalesTaxSvc/PLSAFTCodes",headers=creds) as resp:
           return await resp.json()

async def post_PLSAFTCodes(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PLSAFTCodes
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PLSAFTCodeRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PLSAFTCodeRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SalesTaxSvc/PLSAFTCodes", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_PLSAFTCodes_Company_RateCode_TaxCode_SAFTCode(Company, RateCode, TaxCode, SAFTCode, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PLSAFTCode item
   Description: Calls GetByID to retrieve the PLSAFTCode item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PLSAFTCode
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RateCode: Desc: RateCode   Required: True   Allow empty value : True
      :param TaxCode: Desc: TaxCode   Required: True   Allow empty value : True
      :param SAFTCode: Desc: SAFTCode   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PLSAFTCodeRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.SalesTaxSvc/PLSAFTCodes(" + Company + "," + RateCode + "," + TaxCode + "," + SAFTCode + ")",headers=creds) as resp:
           return await resp.json()

async def patch_PLSAFTCodes_Company_RateCode_TaxCode_SAFTCode(Company, RateCode, TaxCode, SAFTCode, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update PLSAFTCode for the service
   Description: Calls UpdateExt to update PLSAFTCode. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PLSAFTCode
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RateCode: Desc: RateCode   Required: True   Allow empty value : True
      :param TaxCode: Desc: TaxCode   Required: True   Allow empty value : True
      :param SAFTCode: Desc: SAFTCode   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PLSAFTCodeRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.SalesTaxSvc/PLSAFTCodes(" + Company + "," + RateCode + "," + TaxCode + "," + SAFTCode + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_PLSAFTCodes_Company_RateCode_TaxCode_SAFTCode(Company, RateCode, TaxCode, SAFTCode, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete PLSAFTCode item
   Description: Call UpdateExt to delete PLSAFTCode item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PLSAFTCode
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RateCode: Desc: RateCode   Required: True   Allow empty value : True
      :param TaxCode: Desc: TaxCode   Required: True   Allow empty value : True
      :param SAFTCode: Desc: SAFTCode   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.SalesTaxSvc/PLSAFTCodes(" + Company + "," + RateCode + "," + TaxCode + "," + SAFTCode + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.SalesTaxListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.SalesTaxSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseSalesTax, whereClauseLangDesc, whereClauseSalesTRC, whereClauseEntityGLC, whereClauseSalesTxc, whereClauseTaxBox, whereClauseTaxRate, whereClauseEffRateEntityGLC, whereClauseTaxBoxEffRate, whereClauseTaxGRate, whereClausePLSAFTCode, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClauseSalesTax=" + whereClauseSalesTax
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseLangDesc=" + whereClauseLangDesc
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseSalesTRC=" + whereClauseSalesTRC
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseEntityGLC=" + whereClauseEntityGLC
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseSalesTxc=" + whereClauseSalesTxc
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseTaxBox=" + whereClauseTaxBox
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseTaxRate=" + whereClauseTaxRate
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseEffRateEntityGLC=" + whereClauseEffRateEntityGLC
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseTaxBoxEffRate=" + whereClauseTaxBoxEffRate
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseTaxGRate=" + whereClauseTaxGRate
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClausePLSAFTCode=" + whereClausePLSAFTCode
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.SalesTaxSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(taxCode, epicorHeaders = None):
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
   params += "taxCode=" + taxCode

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.SalesTaxSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.SalesTaxSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_ChangeCollectionType(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeCollectionType
   Description: This method resets appropriate values when taxConnectCalc is true.
   OperationID: ChangeCollectionType
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeCollectionType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeCollectionType_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SalesTaxSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeDiscountType(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeDiscountType
   Description: This method resets appropriate values when taxConnectCalc is true.
   OperationID: ChangeDiscountType
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeDiscountType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeDiscountType_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SalesTaxSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeTaxBoxCode(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeTaxBoxCode
   Description: This method validates BoxCode entered and populates the record from TaxBoxDefault.
   OperationID: ChangeTaxBoxCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeTaxBoxCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeTaxBoxCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SalesTaxSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeTaxConnectCalc(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeTaxConnectCalc
   Description: This method resets appropriate values when taxConnectCalc is true.
   OperationID: ChangeTaxConnectCalc
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeTaxConnectCalc_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeTaxConnectCalc_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SalesTaxSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeNumbering(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeNumbering
   Description: This method validates wrong values.
   OperationID: ChangeNumbering
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeNumbering_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeNumbering_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SalesTaxSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeTiming(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeTiming
   Description: This method resets appropriate values ServiceTaxPoint when Timing is 0.
   OperationID: ChangeTiming
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeTiming_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeTiming_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SalesTaxSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeDescription(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeDescription
   OperationID: ChangeDescription
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeDescription_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeDescription_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SalesTaxSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeRateType(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeRateType
   Description: This method checks if Rate Type selected is valid for selected Collection Method.
   OperationID: ChangeRateType
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeRateType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeRateType_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SalesTaxSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewEffRateEntityGLCOver(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewEffRateEntityGLCOver
   Description: This method used to get new EffRateEntityGLC with proper key values.
   OperationID: GetNewEffRateEntityGLCOver
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewEffRateEntityGLCOver_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewEffRateEntityGLCOver_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SalesTaxSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidateEffectiveDate(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateEffectiveDate
   Description: Validate Tax Rate's Effective Date and return a true if effective rate exists for this date.
   OperationID: ValidateEffectiveDate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateEffectiveDate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateEffectiveDate_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SalesTaxSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewTaxBoxEffRateOver(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewTaxBoxEffRateOver
   Description: This method used to get new TaxBoxEffRate with proper key values.
   OperationID: GetNewTaxBoxEffRateOver
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewTaxBoxEffRateOver_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewTaxBoxEffRateOver_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SalesTaxSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeTaxBoxEffRateCode(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeTaxBoxEffRateCode
   Description: This method validates BoxCode entered and populates the record from TaxBoxDefault.
   OperationID: ChangeTaxBoxEffRateCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeTaxBoxEffRateCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeTaxBoxEffRateCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SalesTaxSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CopyTaxBoxEffFromLastEffRate(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CopyTaxBoxEffFromLastEffRate
   Description: Copy TaxBoxEffRate from Last Effective Tax Rate
   OperationID: CopyTaxBoxEffFromLastEffRate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CopyTaxBoxEffFromLastEffRate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CopyTaxBoxEffFromLastEffRate_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SalesTaxSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CopyTaxBoxFromRatesTaxBox(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CopyTaxBoxFromRatesTaxBox
   Description: Copy TaxBoxEffRate from Rates > Tax Boxes
   OperationID: CopyTaxBoxFromRatesTaxBox
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CopyTaxBoxFromRatesTaxBox_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CopyTaxBoxFromRatesTaxBox_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SalesTaxSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DisableCopyTaxBoxFromLastEffRate(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DisableCopyTaxBoxFromLastEffRate
   OperationID: DisableCopyTaxBoxFromLastEffRate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DisableCopyTaxBoxFromLastEffRate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DisableCopyTaxBoxFromLastEffRate_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SalesTaxSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DisableCopyTaxBoxFromRates(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DisableCopyTaxBoxFromRates
   OperationID: DisableCopyTaxBoxFromRates
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DisableCopyTaxBoxFromRates_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DisableCopyTaxBoxFromRates_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SalesTaxSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckPLSAFTCode(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckPLSAFTCode
   Description: SAF-T code validation
   OperationID: CheckPLSAFTCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckPLSAFTCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckPLSAFTCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SalesTaxSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckPLSAFTCodeAndDescUpdate(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckPLSAFTCodeAndDescUpdate
   Description: SAF-T code validation and description getting
   OperationID: CheckPLSAFTCodeAndDescUpdate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckPLSAFTCodeAndDescUpdate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckPLSAFTCodeAndDescUpdate_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SalesTaxSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_UpdatePLSAFTCode(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method UpdatePLSAFTCode
   OperationID: UpdatePLSAFTCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdatePLSAFTCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdatePLSAFTCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SalesTaxSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_LookupPLSAFTCode(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method LookupPLSAFTCode
   OperationID: LookupPLSAFTCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/LookupPLSAFTCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/LookupPLSAFTCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SalesTaxSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_RemovePLSAFTCode(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method RemovePLSAFTCode
   OperationID: RemovePLSAFTCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/RemovePLSAFTCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RemovePLSAFTCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SalesTaxSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_PEChangeUDCode(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method PEChangeUDCode
   Description: This method should be called after SUNAT fields have been changed.
   OperationID: PEChangeUDCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/PEChangeUDCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PEChangeUDCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SalesTaxSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_PEChangeType(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method PEChangeType
   Description: This method should be called after Type field has been changed.
   OperationID: PEChangeType
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/PEChangeType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PEChangeType_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SalesTaxSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetTimingDataForCombo(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetTimingDataForCombo
   OperationID: GetTimingDataForCombo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetTimingDataForCombo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetTimingDataForCombo_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SalesTaxSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetCollectionDataForCombo(epicorHeaders = None):
   """  
   Summary: Invoke method GetCollectionDataForCombo
   Description: Get Data for Collection combobox
   OperationID: GetCollectionDataForCombo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCollectionDataForCombo_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SalesTaxSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_GetRateTypes(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetRateTypes
   Description: Get Data for Effective Rate Rate Types combo.
   OperationID: GetRateTypes
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetRateTypes_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRateTypes_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SalesTaxSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetDiscountTypes(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetDiscountTypes
   Description: Get data for Discount types combo.
   OperationID: GetDiscountTypes
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetDiscountTypes_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDiscountTypes_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SalesTaxSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNumberingValues(epicorHeaders = None):
   """  
   Summary: Invoke method GetNumberingValues
   Description: Get data fo Numbering combo
   OperationID: GetNumberingValues
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNumberingValues_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SalesTaxSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_GetNewSalesTax(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewSalesTax
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewSalesTax
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewSalesTax_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewSalesTax_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SalesTaxSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewLangDesc(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewLangDesc
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewLangDesc
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewLangDesc_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewLangDesc_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SalesTaxSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewSalesTRC(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewSalesTRC
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewSalesTRC
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewSalesTRC_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewSalesTRC_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SalesTaxSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewEntityGLC(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewEntityGLC
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewEntityGLC
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewEntityGLC_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewEntityGLC_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SalesTaxSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewSalesTxc(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewSalesTxc
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewSalesTxc
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewSalesTxc_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewSalesTxc_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SalesTaxSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewTaxBox(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewTaxBox
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewTaxBox
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewTaxBox_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewTaxBox_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SalesTaxSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewTaxRate(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewTaxRate
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewTaxRate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewTaxRate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewTaxRate_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SalesTaxSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewEffRateEntityGLC(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewEffRateEntityGLC
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewEffRateEntityGLC
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewEffRateEntityGLC_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewEffRateEntityGLC_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SalesTaxSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewTaxBoxEffRate(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewTaxBoxEffRate
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewTaxBoxEffRate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewTaxBoxEffRate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewTaxBoxEffRate_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SalesTaxSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewTaxGRate(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewTaxGRate
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewTaxGRate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewTaxGRate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewTaxGRate_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SalesTaxSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewPLSAFTCode(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewPLSAFTCode
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPLSAFTCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPLSAFTCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPLSAFTCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SalesTaxSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SalesTaxSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.SalesTaxSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.SalesTaxSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SalesTaxSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SalesTaxSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_EffRateEntityGLCRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_EffRateEntityGLCRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_EntityGLCRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_EntityGLCRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LangDescRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_LangDescRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PLSAFTCodeRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PLSAFTCodeRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_SalesTRCRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_SalesTRCRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_SalesTaxListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_SalesTaxListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_SalesTaxRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_SalesTaxRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_SalesTxcRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_SalesTxcRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TaxBoxEffRateRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_TaxBoxEffRateRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TaxBoxRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_TaxBoxRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TaxGRateRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_TaxGRateRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TaxRateRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_TaxRateRow] = obj["value"]
      pass

class Erp_Tablesets_EffRateEntityGLCRow:
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
      self.TaxCode:str = obj["TaxCode"]
      self.RateCode:str = obj["RateCode"]
      self.EffectiveFrom:str = obj["EffectiveFrom"]
      self.BitFlag:int = obj["BitFlag"]
      self.GLCntrlDescription:str = obj["GLCntrlDescription"]
      self.GLCntrlTypeDescription:str = obj["GLCntrlTypeDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_EntityGLCRow:
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
      self.BankAcctID:str = obj["BankAcctID"]
      """  BankAcctID of the related BankAcct record.  """  
      self.BankFeeID:str = obj["BankFeeID"]
      self.CallCode:str = obj["CallCode"]
      """  CallCode of the related FSCallCd record.  """  
      self.ChargeCode:str = obj["ChargeCode"]
      self.ClassCode:str = obj["ClassCode"]
      """  ClassCode of the related FAClass record.  """  
      self.ClassID:str = obj["ClassID"]
      """  ClassID.  This can be ClassID of PartClass, PRClsDed, or PRClsTax  """  
      self.ContractCode:str = obj["ContractCode"]
      """  ContractCode of the related FSContCd record.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  CurrencyCode of the related Currency record.  """  
      self.CustNum:int = obj["CustNum"]
      """  CustNum of the related Customer record  """  
      self.DeductionID:str = obj["DeductionID"]
      """  DeductionID of PRClsDed or PRDeduct.  """  
      self.EmpID:str = obj["EmpID"]
      """  EmpID of the related PREmpMas record.  """  
      self.ExpenseCode:str = obj["ExpenseCode"]
      """  ExpenseCode of PayTLbr, LabExpCd  """  
      self.ExtSystemID:str = obj["ExtSystemID"]
      """  ExtSystemID of ExtCompany table  """  
      self.FromPlant:str = obj["FromPlant"]
      """  FromPlant value of the related PlntTranDef record.  """  
      self.GroupCode:str = obj["GroupCode"]
      """  GroupCode of the related FAGroup record.  """  
      self.GroupID:str = obj["GroupID"]
      self.HeadNum:int = obj["HeadNum"]
      self.InvoiceNum:str = obj["InvoiceNum"]
      self.JCDept:str = obj["JCDept"]
      """  JCDept of the related JCDept record.  """  
      self.MiscCode:str = obj["MiscCode"]
      """  MiscCode of the related MiscChrg or PurMisc record.  """  
      self.PartNum:str = obj["PartNum"]
      """  PartNum of the related Part record.  """  
      self.PayTypeID:str = obj["PayTypeID"]
      """  PayTypeID of PayType  """  
      self.PerConName:str = obj["PerConName"]
      self.PIStatus:str = obj["PIStatus"]
      """  PI Status  """  
      self.Plant:str = obj["Plant"]
      """  Plant of the related PlantConfCtrl record.  """  
      self.ProdCode:str = obj["ProdCode"]
      """  ProdCode of the related ProdGrup record.  """  
      self.ProjectID:str = obj["ProjectID"]
      """  ProjectID of the related Project record.  """  
      self.PurchCode:str = obj["PurchCode"]
      """  PurchCode of the related GLPurch record.  """  
      self.RateCode:str = obj["RateCode"]
      """  RateCode of the related GLRate record.  """  
      self.ReasonCode:str = obj["ReasonCode"]
      """  ReasonCode of the related Reason record.  """  
      self.ReasonType:str = obj["ReasonType"]
      """  ReasonType of the related Reason record.  """  
      self.SalesCatID:str = obj["SalesCatID"]
      """  SalesCatID of the related SalesCat record.  """  
      self.Shift:int = obj["Shift"]
      """  Shift value of the related JCShift record.  """  
      self.TaxCode:str = obj["TaxCode"]
      """  TaxCode of the related SalesTax record.  """  
      self.TaxTblID:str = obj["TaxTblID"]
      """  TaxTblID of PRTaxMas or PRClsTax.  """  
      self.ToPlant:str = obj["ToPlant"]
      """  ToPlant value of the related PlntTranDef record.  """  
      self.TransferMethod:str = obj["TransferMethod"]
      """  TransferMethod of ExtCompany table  """  
      self.TypeID:str = obj["TypeID"]
      """  Type ID  """  
      self.VendorNum:int = obj["VendorNum"]
      """  VendorNum of the related Vendor record.  """  
      self.WarehouseCode:str = obj["WarehouseCode"]
      """  WarehouseCode of the related Warehse record.  """  
      self.ExpenseTypeCode:str = obj["ExpenseTypeCode"]
      self.IsFiltered:bool = obj["IsFiltered"]
      self.OprTypeCode:str = obj["OprTypeCode"]
      self.CashDeskID:str = obj["CashDeskID"]
      self.TIN:str = obj["TIN"]
      self.ReclassCodeID:str = obj["ReclassCodeID"]
      self.BitFlag:int = obj["BitFlag"]
      self.GLCntrlDescription:str = obj["GLCntrlDescription"]
      self.GLCntrlTypeDescription:str = obj["GLCntrlTypeDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_LangDescRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.TableName:str = obj["TableName"]
      """  Name of table that this data is related  """  
      self.LangNameID:str = obj["LangNameID"]
      """  Language ID  """  
      self.Key1:str = obj["Key1"]
      """  Contains values that represent the key1 to the foreign record that this record is related.  """  
      self.Key2:str = obj["Key2"]
      """  key2  of  the foreign record  """  
      self.Key3:str = obj["Key3"]
      """  key3 of the foreign record  """  
      self.Description:str = obj["Description"]
      """  Language Description  """  
      self.GlobalLangDesc:bool = obj["GlobalLangDesc"]
      """  Marks this LangDesc as global, available to be sent out to other companies.  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Disables this record from receiving global updates.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.LangNameIDDescription:str = obj["LangNameIDDescription"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PLSAFTCodeRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.RateCode:str = obj["RateCode"]
      """  RateCode  """  
      self.TaxCode:str = obj["TaxCode"]
      """  TaxCode  """  
      self.SAFTCode:str = obj["SAFTCode"]
      """  SAFTCode  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.CodeDesc:str = obj["CodeDesc"]
      self.LongDesc:str = obj["LongDesc"]
      self.TempSAFTCode:str = obj["TempSAFTCode"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_SalesTRCRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.TaxCode:str = obj["TaxCode"]
      """  Descriptive code assigned by user which uniquely identifies a Sales Tax master record.  Can't be blank. This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited.  """  
      self.RateCode:str = obj["RateCode"]
      """  Rate Code  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.DefaultRate:bool = obj["DefaultRate"]
      """  Default Rate  """  
      self.TextCode:str = obj["TextCode"]
      """  Legal Text code  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.AGAFIPCode:str = obj["AGAFIPCode"]
      """  AGAFIPCode  """  
      self.AGFEAFIPCode:str = obj["AGFEAFIPCode"]
      """  AGFEAFIPCode  """  
      self.AGPurchaseColNumber:int = obj["AGPurchaseColNumber"]
      """  AGPurchaseColNumber  """  
      self.AGSalesColNumber:int = obj["AGSalesColNumber"]
      """  AGSalesColNumber  """  
      self.BEIntracomCode:str = obj["BEIntracomCode"]
      """  Intracom Code (CSF Belgium)  """  
      self.JPConsumptionTax:bool = obj["JPConsumptionTax"]
      """  JPConsumptionTax  """  
      self.PLSAFTCode:str = obj["PLSAFTCode"]
      """  PLSAFTCode  """  
      self.CODIANCode:str = obj["CODIANCode"]
      """  CODIANCode  """  
      self.ExternalTaxCategory:str = obj["ExternalTaxCategory"]
      """  UNCL5305  """  
      self.FatherDeleted:bool = obj["FatherDeleted"]
      """  Indicate if is tring to be deleted from SalesTax  """  
      self.BitFlag:int = obj["BitFlag"]
      self.TaxTextDescription:str = obj["TaxTextDescription"]
      self.XbSystELIEinvoice:bool = obj["XbSystELIEinvoice"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_SalesTaxListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.TaxCode:str = obj["TaxCode"]
      """  Descriptive code assigned by user which uniquely identifies a Sales Tax master record.  Can't be blank. This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited.  """  
      self.Description:str = obj["Description"]
      """  Full description for a  Sales Tax master.  """  
      self.Manual:bool = obj["Manual"]
      """  Indicates if the tax calculations are to be performed manually.  This field is used as a default for the InvcTax.Manual field.  When this field is set in the InvcTax record the InvcTax.Reportable, InvcTax.TaxableAmt, and InvcTax.TaxAmount fields are enabled.  When it is NOT set these fields are DISABLED and the system will perform all of the Reportable, Taxable, and TaxAmount calculations automatically.  """  
      self.RoundDown:bool = obj["RoundDown"]
      """  Indicates if set to Yes that any decimal values of a penny/cent should be rounded down rather than rounded to nearest penny/cent.  """  
      self.Advanced:bool = obj["Advanced"]
      """  When checked the sales tax code will apply to advanced billing invoices, and will only apply to additional sums on final invoices.  """  
      self.TaxConnectCalc:bool = obj["TaxConnectCalc"]
      """  Indicates whether taxes related to this Sales Tax ID are calculated via Epicor Tax Connect interface. Default is No.  """  
      self.ETCJurisKey:str = obj["ETCJurisKey"]
      """  If this SalesTax id is used by TaxConnect, this is a string containing the data required to uniquely identify a specific taxing jurisdiction using the tax connect system data. It will be used to generate the ETCHash field. If multiple fields from the tax connect system are required to generate a unique key, they should be concatenated, separated by ?:?. For Avalara it will be the StateJurisCode+ ?:? + TaxDetail JurisCode + ?:? + TaxDetail JurisName returned by the GetTax function for each tax amount. Default is null.  """  
      self.ETCHash:int = obj["ETCHash"]
      """  If this SalesTax id is used by TaxConnect, this is the hash field to be used to cross reference the key fields provided by the tax connect service (stored in ETCJurisKey)  with the Epicor SalesTax id of this record in order to obtain the correct tax accrual GLs for the transaction. Default is null.  """  
      self.CollectionType:int = obj["CollectionType"]
      """  Collection Type  """  
      self.Timing:int = obj["Timing"]
      """  Timing of when to report taxes (default)  """  
      self.Algorithm:str = obj["Algorithm"]
      """  Algorithm  """  
      self.DiscountType:int = obj["DiscountType"]
      """  Discount Types, none, payment discount affect tax, terms discount affect tax  """  
      self.TaxJurisCode:str = obj["TaxJurisCode"]
      """  Tax Jurisdiction  """  
      self.RptCatCode:str = obj["RptCatCode"]
      """  Tax Report Category  """  
      self.TextCode:str = obj["TextCode"]
      """  Legal Text Code  """  
      self.InPrice:bool = obj["InPrice"]
      """  In Price  """  
      self.LglNumType:int = obj["LglNumType"]
      """  Tax Certificate Numbering method  """  
      self.LglNumSeq:int = obj["LglNumSeq"]
      """  Legal Number Sequence  """  
      self.RevRptCatCode:str = obj["RevRptCatCode"]
      """  Reverse Tax Report Category  """  
      self.ServiceTaxPoint:bool = obj["ServiceTaxPoint"]
      """  Intra-EU Service  """  
      self.Direct:str = obj["Direct"]
      """  Sales List Type Indicator  """  
      self.Triangulation:str = obj["Triangulation"]
      """  Sales List Type Indicator  """  
      self.GlobalSalesTax:bool = obj["GlobalSalesTax"]
      """  Marks this SalesTax as global, available to be sent out to other companies.  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Disables this record from receiving global updates.  """  
      self.InvoiceType:str = obj["InvoiceType"]
      """  Invoice Type: 0-No Vat Reporting, 1-Tax Invoice, 2-Duty-Free Invoice  """  
      self.InvMethod:str = obj["InvMethod"]
      """  Invoicing Method: 0-No VAT Reporting, 1-Paper Invoice, 2-eInvoice, 3-No Invoice  """  
      self.CustType:str = obj["CustType"]
      """  Customer Type: 0-No VAT Reporting, 1-Company Sales, 2-Personal Sales  """  
      self.RevType:str = obj["RevType"]
      """  Revenue Type: 0-No VAT Reporting, 1-Trading Revenue, 2-Non-Trading Revenue  """  
      self.IssueType:str = obj["IssueType"]
      """  Issue Type: 0-No VAT Reporting, 1-Normal Invoice, 2-Issued by Supplier  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.ParentJurisdiction:str = obj["ParentJurisdiction"]
      """  Parent Tax Id  """  
      self.EnableRevCharge:bool = obj["EnableRevCharge"]
      """  Flag to indicate if Reverse Charge should be enabled.  """  
      self.EnableTaxBox:bool = obj["EnableTaxBox"]
      """  Flag to indicate if Tax Box maintenance should be allowed.  """  
      self.mtlDescription:str = obj["mtlDescription"]
      """  Description of the record, translated in the selected language  """  
      self.mtlLangDesc:str = obj["mtlLangDesc"]
      """  Name of the selected language of Description  """  
      self.mtlLangId:str = obj["mtlLangId"]
      """  ID of the selected language  """  
      self.TaxAlgrmDescription:str = obj["TaxAlgrmDescription"]
      """  Description  """  
      self.TaxJurisDescription:str = obj["TaxJurisDescription"]
      """  Description  """  
      self.TaxRptCatDescription:str = obj["TaxRptCatDescription"]
      """  Description  """  
      self.TaxTextDescription:str = obj["TaxTextDescription"]
      """  Description  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_SalesTaxRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.TaxCode:str = obj["TaxCode"]
      """  Descriptive code assigned by user which uniquely identifies a Sales Tax master record.  Can't be blank. This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited.  """  
      self.Description:str = obj["Description"]
      """  Full description for a  Sales Tax master.  """  
      self.Manual:bool = obj["Manual"]
      """  Indicates if the tax calculations are to be performed manually.  This field is used as a default for the InvcTax.Manual field.  When this field is set in the InvcTax record the InvcTax.Reportable, InvcTax.TaxableAmt, and InvcTax.TaxAmount fields are enabled.  When it is NOT set these fields are DISABLED and the system will perform all of the Reportable, Taxable, and TaxAmount calculations automatically.  """  
      self.RoundDown:bool = obj["RoundDown"]
      """  Indicates if set to Yes that any decimal values of a penny/cent should be rounded down rather than rounded to nearest penny/cent.  """  
      self.Advanced:bool = obj["Advanced"]
      """  When checked the sales tax code will apply to advanced billing invoices, and will only apply to additional sums on final invoices.  """  
      self.TaxConnectCalc:bool = obj["TaxConnectCalc"]
      """  Indicates whether taxes related to this Sales Tax ID are calculated via Epicor Tax Connect interface. Default is No.  """  
      self.ETCJurisKey:str = obj["ETCJurisKey"]
      """  If this SalesTax id is used by TaxConnect, this is a string containing the data required to uniquely identify a specific taxing jurisdiction using the tax connect system data. It will be used to generate the ETCHash field. If multiple fields from the tax connect system are required to generate a unique key, they should be concatenated, separated by ?:?. For Avalara it will be the StateJurisCode+ ?:? + TaxDetail JurisCode + ?:? + TaxDetail JurisName returned by the GetTax function for each tax amount. Default is null.  """  
      self.ETCHash:int = obj["ETCHash"]
      """  If this SalesTax id is used by TaxConnect, this is the hash field to be used to cross reference the key fields provided by the tax connect service (stored in ETCJurisKey)  with the Epicor SalesTax id of this record in order to obtain the correct tax accrual GLs for the transaction. Default is null.  """  
      self.CollectionType:int = obj["CollectionType"]
      """  Collection Type  """  
      self.Timing:int = obj["Timing"]
      """  Timing of when to report taxes (default)  """  
      self.Algorithm:str = obj["Algorithm"]
      """  Algorithm  """  
      self.DiscountType:int = obj["DiscountType"]
      """  Discount Types, none, payment discount affect tax, terms discount affect tax  """  
      self.TaxJurisCode:str = obj["TaxJurisCode"]
      """  Tax Jurisdiction  """  
      self.RptCatCode:str = obj["RptCatCode"]
      """  Tax Report Category  """  
      self.TextCode:str = obj["TextCode"]
      """  Legal Text Code  """  
      self.InPrice:bool = obj["InPrice"]
      """  In Price  """  
      self.LglNumType:int = obj["LglNumType"]
      """  Tax Certificate Numbering method  """  
      self.LglNumSeq:int = obj["LglNumSeq"]
      """  Legal Number Sequence  """  
      self.RevRptCatCode:str = obj["RevRptCatCode"]
      """  Reverse Tax Report Category  """  
      self.ServiceTaxPoint:bool = obj["ServiceTaxPoint"]
      """  Intra-EU Service  """  
      self.Direct:str = obj["Direct"]
      """  Sales List Type Indicator  """  
      self.Triangulation:str = obj["Triangulation"]
      """  Sales List Type Indicator  """  
      self.GlobalSalesTax:bool = obj["GlobalSalesTax"]
      """  Marks this SalesTax as global, available to be sent out to other companies.  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Disables this record from receiving global updates.  """  
      self.InvoiceType:str = obj["InvoiceType"]
      """  Invoice Type: 0-No Vat Reporting, 1-Tax Invoice, 2-Duty-Free Invoice  """  
      self.InvMethod:str = obj["InvMethod"]
      """  Invoicing Method: 0-No VAT Reporting, 1-Paper Invoice, 2-eInvoice, 3-No Invoice  """  
      self.CustType:str = obj["CustType"]
      """  Customer Type: 0-No VAT Reporting, 1-Company Sales, 2-Personal Sales  """  
      self.RevType:str = obj["RevType"]
      """  Revenue Type: 0-No VAT Reporting, 1-Trading Revenue, 2-Non-Trading Revenue  """  
      self.IssueType:str = obj["IssueType"]
      """  Issue Type: 0-No VAT Reporting, 1-Normal Invoice, 2-Issued by Supplier  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.INIsCST:bool = obj["INIsCST"]
      """  INIsCST  """  
      self.AGAFIPCode:str = obj["AGAFIPCode"]
      """  AGAFIPCode  """  
      self.AGAFIPTaxRegCode:str = obj["AGAFIPTaxRegCode"]
      """  AGAFIPTaxRegCode  """  
      self.AGAFIPTaxRegDesc:str = obj["AGAFIPTaxRegDesc"]
      """  AGAFIPTaxRegDesc  """  
      self.AGMinimumByTax:bool = obj["AGMinimumByTax"]
      """  AGMinimumByTax  """  
      self.AGTaxableAmtType:str = obj["AGTaxableAmtType"]
      """  AGTaxableAmtType  """  
      self.AGWHHeader:str = obj["AGWHHeader"]
      """  AGWHHeader  """  
      self.IndirectTaxType:str = obj["IndirectTaxType"]
      """  IndirectTaxType  """  
      self.MXTaxCategory:str = obj["MXTaxCategory"]
      """  Mexico Localizaion field to store TaxType Category for Mexico  """  
      self.NOTaxCategory:str = obj["NOTaxCategory"]
      """  NOTaxCategory  """  
      self.PETranDocTypeID:str = obj["PETranDocTypeID"]
      """  PETranDocTypeID  """  
      self.PETaxOriginType:str = obj["PETaxOriginType"]
      """  PETaxOriginType  """  
      self.MXSATCode:str = obj["MXSATCode"]
      """  MXSATCode  """  
      self.PESUNATCode:str = obj["PESUNATCode"]
      """  PE SUNAT Code  """  
      self.PESUNATName:str = obj["PESUNATName"]
      """  PE SUNAT Name  """  
      self.PESUNATType:str = obj["PESUNATType"]
      """  PE SUNAT Type  """  
      self.PLSAFTCode:str = obj["PLSAFTCode"]
      """  PLSAFTCode  """  
      self.MXTaxType:str = obj["MXTaxType"]
      """  MXTaxType  """  
      self.MXTypeFactor:str = obj["MXTypeFactor"]
      """  MXTypeFactor  """  
      self.SendToFSA:bool = obj["SendToFSA"]
      """  Determines if the tax type has to be synchronized with Epicor FSA application.  """  
      self.TimingDepositAdvBilling:int = obj["TimingDepositAdvBilling"]
      """  Timing of when to report taxes (specific to Deposit Billing and Advanced Billing invoices)  """  
      self.EInvTaxCategory:str = obj["EInvTaxCategory"]
      """  E-Invoice Tax Category  """  
      self.PEISCCalcCode:str = obj["PEISCCalcCode"]
      """  PEISCCalcCode  """  
      self.PEAllowanceChargeReasonCode:str = obj["PEAllowanceChargeReasonCode"]
      """  PEAllowanceChargeReasonCode  """  
      self.ExternalTaxCategory:str = obj["ExternalTaxCategory"]
      """  Tax category; Country specific, e.g. ‘GST’ for ANZ. UNTDID 5153  """  
      self.AllowConfirmationTax:bool = obj["AllowConfirmationTax"]
      self.EnableRevCharge:bool = obj["EnableRevCharge"]
      """  Flag to indicate if Reverse Charge should be enabled.  """  
      self.EnableTaxBox:bool = obj["EnableTaxBox"]
      """  Flag to indicate if Tax Box maintenance should be allowed.  """  
      self.mtlDescription:str = obj["mtlDescription"]
      """  Description of the record, translated in the selected language  """  
      self.mtlLangDesc:str = obj["mtlLangDesc"]
      """  Name of the selected language of Description  """  
      self.mtlLangId:str = obj["mtlLangId"]
      """  ID of the selected language  """  
      self.ParentJurisdiction:str = obj["ParentJurisdiction"]
      """  Parent Tax Id  """  
      self.PEISCCalcCodeDesc:str = obj["PEISCCalcCodeDesc"]
      self.PESUNATCodeDesc:str = obj["PESUNATCodeDesc"]
      self.EnableChanges:bool = obj["EnableChanges"]
      """  Flag to indicate if the tax type is assigned to a tax liability.  """  
      self.PEAllowanceChargeReasonDesc:str = obj["PEAllowanceChargeReasonDesc"]
      """  Peru CSF: Allowance Change Reason Code description  """  
      self.BitFlag:int = obj["BitFlag"]
      self.CompanySendToFSA:bool = obj["CompanySendToFSA"]
      self.TaxAlgrmDescription:str = obj["TaxAlgrmDescription"]
      self.TaxJurisDescription:str = obj["TaxJurisDescription"]
      self.TaxRptCatDescription:str = obj["TaxRptCatDescription"]
      self.TaxTextDescription:str = obj["TaxTextDescription"]
      self.XbSystELIEinvoice:bool = obj["XbSystELIEinvoice"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_SalesTxcRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.TaxCode:str = obj["TaxCode"]
      """  The TaxCode to which this record is related.  """  
      self.TaxCatID:str = obj["TaxCatID"]
      """  The TaxCatID which relates this record to the TaxCat record.  """  
      self.Reportable:bool = obj["Reportable"]
      """  Indicates that sales made of tax category are still reportable to the taxing jurisdiction as gross receipts even thou this category is  not  taxable.  """  
      self.RateCode:str = obj["RateCode"]
      """  Rate Code  """  
      self.ExemptType:int = obj["ExemptType"]
      """  Exemption Type  """  
      self.ExemptPercent:int = obj["ExemptPercent"]
      """  Exemption Percent  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.TaxCatIDDesc:str = obj["TaxCatIDDesc"]
      """  Tax category description  """  
      self.BitFlag:int = obj["BitFlag"]
      self.TaxCatIDDescription:str = obj["TaxCatIDDescription"]
      self.TaxCodeDescription:str = obj["TaxCodeDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_TaxBoxEffRateRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.TaxCode:str = obj["TaxCode"]
      """  TaxCode  """  
      self.BoxCode:str = obj["BoxCode"]
      """  BoxCode  """  
      self.SourceModule:str = obj["SourceModule"]
      """  SourceModule  """  
      self.AmountType:str = obj["AmountType"]
      """  AmountType  """  
      self.ECAcquisitionSeq:int = obj["ECAcquisitionSeq"]
      """  ECAcquisitionSeq  """  
      self.EffectiveFrom:str = obj["EffectiveFrom"]
      """  EffectiveFrom  """  
      self.BoxSign:str = obj["BoxSign"]
      """  BoxSign  """  
      self.RateCode:str = obj["RateCode"]
      """  RateCode  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.BoxCodeDescription:str = obj["BoxCodeDescription"]
      """  Box Code Description  """  
      self.EnableTaxBox:bool = obj["EnableTaxBox"]
      """  Flag to indicate if Tax Box maintenance should be allowed.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_TaxBoxRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.TaxCode:str = obj["TaxCode"]
      """  Descriptive code assigned by user which uniquely identifies a Sales Tax master record.  Can't be blank. This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited.  """  
      self.BoxCode:str = obj["BoxCode"]
      """  Tax Box Code.  """  
      self.SourceModule:str = obj["SourceModule"]
      """   Indicates the source module of the transaction for this tax box.
Possible values are: "AR" = from AR Invoice;  "AP" = from AP Invoice;  "ARCM" = from AR Credit Memo;  "APDM" = from AP Debit Memo.  """  
      self.AmountType:str = obj["AmountType"]
      """  The Amount type to be stored for this tax box.  The possible values are:  "Tax" = for Tax Amount; "Taxable" = for Taxable Amount.  """  
      self.ECAcquisitionSeq:int = obj["ECAcquisitionSeq"]
      """  Indicates if the tax line associated with this tax box is the Primary or Secondary line. This field corresponds to the ECAcquisitionSeq stored in the APInvTax to indicate the second reversing tax line.  Valid values are: 0 = Primary or Standard tax line;  1 = Secondary or Reversing tax line (only created if ECAcquisition or Reverse Charge apply)  """  
      self.BoxSign:str = obj["BoxSign"]
      """  Sign for box amount. + means add the taxable/tax amount to the (taxable/tax) box value; - means substract the taxable/tax amount from the (taxable/tax) box value.  """  
      self.RateCode:str = obj["RateCode"]
      """  Rate Code  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.EnableTaxBox:bool = obj["EnableTaxBox"]
      """  Flag to indicate if Tax Box maintenance should be allowed.  """  
      self.BoxCodeDescription:str = obj["BoxCodeDescription"]
      """  Box Code Description  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_TaxGRateRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.TaxCode:str = obj["TaxCode"]
      """  Descriptive code assigned by user which uniquely identifies a Sales Tax master record.  Can't be blank. This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited.  """  
      self.RateCode:str = obj["RateCode"]
      """  Tax Rate Code  """  
      self.EffectiveFrom:str = obj["EffectiveFrom"]
      """  First date tax rate is valid for  """  
      self.FromAmount:int = obj["FromAmount"]
      """  Minimum amount to apply tax to  """  
      self.TaxPercent:int = obj["TaxPercent"]
      """  Tax Percent to use  """  
      self.TaxAmount:int = obj["TaxAmount"]
      """  Fixed Tax Amount to apply  """  
      self.ReverseCharge:bool = obj["ReverseCharge"]
      """  Reverse Charge  """  
      self.TextCode:str = obj["TextCode"]
      """  Unique Identifier for Legal Text  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.ReverseAvail:bool = obj["ReverseAvail"]
      """  Flag to indicate if Reverse Charge check box is available to the user  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      self.BitFlag:int = obj["BitFlag"]
      self.TaxTextDescription:str = obj["TaxTextDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_TaxRateRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.TaxCode:str = obj["TaxCode"]
      """  Descriptive code assigned by user which uniquely identifies a Sales Tax master record.  Can't be blank. This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited.  """  
      self.RateCode:str = obj["RateCode"]
      """  Rate Code  """  
      self.EffectiveFrom:str = obj["EffectiveFrom"]
      """  First date tax rate is valid for  """  
      self.RateType:int = obj["RateType"]
      """  Percentage, Fixed Value or Graduated Rate  """  
      self.TaxPercent:int = obj["TaxPercent"]
      """  Tax Percent  """  
      self.TaxAmount:int = obj["TaxAmount"]
      """  Fixed Tax Amount  """  
      self.DeductPercent:int = obj["DeductPercent"]
      """  Deduction Percent  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  Currency Code  """  
      self.MinAmount:int = obj["MinAmount"]
      """  Minimum Amount  """  
      self.MaxAmount:int = obj["MaxAmount"]
      """  Maximum Amount  """  
      self.CentCode:str = obj["CentCode"]
      """  Cent Override Code  """  
      self.CompMethod:str = obj["CompMethod"]
      """  I - Document Level, L - Line Level  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.PEMinInvAmt:int = obj["PEMinInvAmt"]
      """  PEMinInvAmt  """  
      self.PEMinPayAmt:int = obj["PEMinPayAmt"]
      """  PEMinPayAmt  """  
      self.PEIncTaxAmt:bool = obj["PEIncTaxAmt"]
      """  PEIncTaxAmt  """  
      self.PEWHCurrencyCode:str = obj["PEWHCurrencyCode"]
      """  PEWHCurrencyCode  """  
      self.DisableDeduct:bool = obj["DisableDeduct"]
      """  Indicates if Deduct percent is not available for changes (always 100%)  """  
      self.DspTaxPercent:int = obj["DspTaxPercent"]
      """  PatchField for TaxPercent (using 3 decimals instead of 2)  """  
      self.EnableCopyTaxBoxFromLEffRate:bool = obj["EnableCopyTaxBoxFromLEffRate"]
      """  Enable copy Tax Boxes from Last Effective Rate  """  
      self.EnableCopyTaxBoxFromRates:bool = obj["EnableCopyTaxBoxFromRates"]
      """  Enable button copy Tax Boxes from Tax Rate Boxes  """  
      self.CollectionType:int = obj["CollectionType"]
      """  Like SalesTax.CollectionType - for technical purpose  """  
      self.BitFlag:int = obj["BitFlag"]
      self.CurrencyCurrName:str = obj["CurrencyCurrName"]
      self.CurrencyDocumentDesc:str = obj["CurrencyDocumentDesc"]
      self.CurrencyCurrDesc:str = obj["CurrencyCurrDesc"]
      self.CurrencyCurrencyID:str = obj["CurrencyCurrencyID"]
      self.CurrencyCurrSymbol:str = obj["CurrencyCurrSymbol"]
      self.TaxCentDescription:str = obj["TaxCentDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class ChangeCollectionType_input:
   """ Required : 
   proposedCollectionType
   ds
   """  
   def __init__(self, obj):
      self.proposedCollectionType:int = obj["proposedCollectionType"]
      """  The proposed Tax Collection Type.  """  
      self.ds:list[Erp_Tablesets_SalesTaxTableset] = obj["ds"]
      pass

class ChangeCollectionType_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_SalesTaxTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeDescription_input:
   """ Required : 
   Description
   ds
   """  
   def __init__(self, obj):
      self.Description:str = obj["Description"]
      self.ds:list[Erp_Tablesets_SalesTaxTableset] = obj["ds"]
      pass

class ChangeDescription_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_SalesTaxTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeDiscountType_input:
   """ Required : 
   proposedDiscountType
   ds
   """  
   def __init__(self, obj):
      self.proposedDiscountType:int = obj["proposedDiscountType"]
      """  The proposed Discount Type value.  """  
      self.ds:list[Erp_Tablesets_SalesTaxTableset] = obj["ds"]
      pass

class ChangeDiscountType_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_SalesTaxTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeNumbering_input:
   """ Required : 
   proposedNumbering
   ds
   """  
   def __init__(self, obj):
      self.proposedNumbering:int = obj["proposedNumbering"]
      """  The proposed Numbering.  """  
      self.ds:list[Erp_Tablesets_SalesTaxTableset] = obj["ds"]
      pass

class ChangeNumbering_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_SalesTaxTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeRateType_input:
   """ Required : 
   ds
   proposedRateType
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_SalesTaxTableset] = obj["ds"]
      self.proposedRateType:int = obj["proposedRateType"]
      """  The proposed Rate Type.  """  
      pass

class ChangeRateType_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_SalesTaxTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeTaxBoxCode_input:
   """ Required : 
   proposedBoxCode
   ds
   """  
   def __init__(self, obj):
      self.proposedBoxCode:str = obj["proposedBoxCode"]
      """  The proposed BoxCode value.  """  
      self.ds:list[Erp_Tablesets_SalesTaxTableset] = obj["ds"]
      pass

class ChangeTaxBoxCode_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_SalesTaxTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeTaxBoxEffRateCode_input:
   """ Required : 
   proposedBoxCode
   ds
   """  
   def __init__(self, obj):
      self.proposedBoxCode:str = obj["proposedBoxCode"]
      """  The proposed BoxCode value.  """  
      self.ds:list[Erp_Tablesets_SalesTaxTableset] = obj["ds"]
      pass

class ChangeTaxBoxEffRateCode_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_SalesTaxTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeTaxConnectCalc_input:
   """ Required : 
   proposedTaxConnectCalc
   ds
   """  
   def __init__(self, obj):
      self.proposedTaxConnectCalc:bool = obj["proposedTaxConnectCalc"]
      """  The proposed TaxConnectCalc value.  """  
      self.ds:list[Erp_Tablesets_SalesTaxTableset] = obj["ds"]
      pass

class ChangeTaxConnectCalc_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_SalesTaxTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeTiming_input:
   """ Required : 
   proposedTiming
   ds
   """  
   def __init__(self, obj):
      self.proposedTiming:int = obj["proposedTiming"]
      """  The proposed Timing.  """  
      self.ds:list[Erp_Tablesets_SalesTaxTableset] = obj["ds"]
      pass

class ChangeTiming_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_SalesTaxTableset] = obj["ds"]
      pass

      """  output parameters  """  

class CheckPLSAFTCodeAndDescUpdate_input:
   """ Required : 
   newSAFTCode
   ds
   """  
   def __init__(self, obj):
      self.newSAFTCode:str = obj["newSAFTCode"]
      self.ds:list[Erp_Tablesets_SalesTaxTableset] = obj["ds"]
      pass

class CheckPLSAFTCodeAndDescUpdate_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_SalesTaxTableset] = obj["ds"]
      pass

      """  output parameters  """  

class CheckPLSAFTCode_input:
   """ Required : 
   code
   """  
   def __init__(self, obj):
      self.code:str = obj["code"]
      """  SAF-T Code  """  
      pass

class CheckPLSAFTCode_output:
   def __init__(self, obj):
      pass

class CopyTaxBoxEffFromLastEffRate_input:
   """ Required : 
   ds
   taxCode
   rateCode
   effectiveFrom
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_SalesTaxTableset] = obj["ds"]
      self.taxCode:str = obj["taxCode"]
      self.rateCode:str = obj["rateCode"]
      self.effectiveFrom:str = obj["effectiveFrom"]
      pass

class CopyTaxBoxEffFromLastEffRate_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_SalesTaxTableset] = obj["ds"]
      pass

      """  output parameters  """  

class CopyTaxBoxFromRatesTaxBox_input:
   """ Required : 
   ds
   taxCode
   rateCode
   effectiveFrom
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_SalesTaxTableset] = obj["ds"]
      self.taxCode:str = obj["taxCode"]
      self.rateCode:str = obj["rateCode"]
      self.effectiveFrom:str = obj["effectiveFrom"]
      pass

class CopyTaxBoxFromRatesTaxBox_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_SalesTaxTableset] = obj["ds"]
      pass

      """  output parameters  """  

class DeleteByID_input:
   """ Required : 
   taxCode
   """  
   def __init__(self, obj):
      self.taxCode:str = obj["taxCode"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class DisableCopyTaxBoxFromLastEffRate_input:
   """ Required : 
   taxCode
   rateCode
   effectiveFrom
   """  
   def __init__(self, obj):
      self.taxCode:str = obj["taxCode"]
      self.rateCode:str = obj["rateCode"]
      self.effectiveFrom:str = obj["effectiveFrom"]
      pass

class DisableCopyTaxBoxFromLastEffRate_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      pass

class DisableCopyTaxBoxFromRates_input:
   """ Required : 
   taxCode
   rateCode
   effectiveFrom
   """  
   def __init__(self, obj):
      self.taxCode:str = obj["taxCode"]
      self.rateCode:str = obj["rateCode"]
      self.effectiveFrom:str = obj["effectiveFrom"]
      pass

class DisableCopyTaxBoxFromRates_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      pass

class Erp_Tablesets_EffRateEntityGLCRow:
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
      self.TaxCode:str = obj["TaxCode"]
      self.RateCode:str = obj["RateCode"]
      self.EffectiveFrom:str = obj["EffectiveFrom"]
      self.BitFlag:int = obj["BitFlag"]
      self.GLCntrlDescription:str = obj["GLCntrlDescription"]
      self.GLCntrlTypeDescription:str = obj["GLCntrlTypeDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_EntityGLCRow:
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
      self.BankAcctID:str = obj["BankAcctID"]
      """  BankAcctID of the related BankAcct record.  """  
      self.BankFeeID:str = obj["BankFeeID"]
      self.CallCode:str = obj["CallCode"]
      """  CallCode of the related FSCallCd record.  """  
      self.ChargeCode:str = obj["ChargeCode"]
      self.ClassCode:str = obj["ClassCode"]
      """  ClassCode of the related FAClass record.  """  
      self.ClassID:str = obj["ClassID"]
      """  ClassID.  This can be ClassID of PartClass, PRClsDed, or PRClsTax  """  
      self.ContractCode:str = obj["ContractCode"]
      """  ContractCode of the related FSContCd record.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  CurrencyCode of the related Currency record.  """  
      self.CustNum:int = obj["CustNum"]
      """  CustNum of the related Customer record  """  
      self.DeductionID:str = obj["DeductionID"]
      """  DeductionID of PRClsDed or PRDeduct.  """  
      self.EmpID:str = obj["EmpID"]
      """  EmpID of the related PREmpMas record.  """  
      self.ExpenseCode:str = obj["ExpenseCode"]
      """  ExpenseCode of PayTLbr, LabExpCd  """  
      self.ExtSystemID:str = obj["ExtSystemID"]
      """  ExtSystemID of ExtCompany table  """  
      self.FromPlant:str = obj["FromPlant"]
      """  FromPlant value of the related PlntTranDef record.  """  
      self.GroupCode:str = obj["GroupCode"]
      """  GroupCode of the related FAGroup record.  """  
      self.GroupID:str = obj["GroupID"]
      self.HeadNum:int = obj["HeadNum"]
      self.InvoiceNum:str = obj["InvoiceNum"]
      self.JCDept:str = obj["JCDept"]
      """  JCDept of the related JCDept record.  """  
      self.MiscCode:str = obj["MiscCode"]
      """  MiscCode of the related MiscChrg or PurMisc record.  """  
      self.PartNum:str = obj["PartNum"]
      """  PartNum of the related Part record.  """  
      self.PayTypeID:str = obj["PayTypeID"]
      """  PayTypeID of PayType  """  
      self.PerConName:str = obj["PerConName"]
      self.PIStatus:str = obj["PIStatus"]
      """  PI Status  """  
      self.Plant:str = obj["Plant"]
      """  Plant of the related PlantConfCtrl record.  """  
      self.ProdCode:str = obj["ProdCode"]
      """  ProdCode of the related ProdGrup record.  """  
      self.ProjectID:str = obj["ProjectID"]
      """  ProjectID of the related Project record.  """  
      self.PurchCode:str = obj["PurchCode"]
      """  PurchCode of the related GLPurch record.  """  
      self.RateCode:str = obj["RateCode"]
      """  RateCode of the related GLRate record.  """  
      self.ReasonCode:str = obj["ReasonCode"]
      """  ReasonCode of the related Reason record.  """  
      self.ReasonType:str = obj["ReasonType"]
      """  ReasonType of the related Reason record.  """  
      self.SalesCatID:str = obj["SalesCatID"]
      """  SalesCatID of the related SalesCat record.  """  
      self.Shift:int = obj["Shift"]
      """  Shift value of the related JCShift record.  """  
      self.TaxCode:str = obj["TaxCode"]
      """  TaxCode of the related SalesTax record.  """  
      self.TaxTblID:str = obj["TaxTblID"]
      """  TaxTblID of PRTaxMas or PRClsTax.  """  
      self.ToPlant:str = obj["ToPlant"]
      """  ToPlant value of the related PlntTranDef record.  """  
      self.TransferMethod:str = obj["TransferMethod"]
      """  TransferMethod of ExtCompany table  """  
      self.TypeID:str = obj["TypeID"]
      """  Type ID  """  
      self.VendorNum:int = obj["VendorNum"]
      """  VendorNum of the related Vendor record.  """  
      self.WarehouseCode:str = obj["WarehouseCode"]
      """  WarehouseCode of the related Warehse record.  """  
      self.ExpenseTypeCode:str = obj["ExpenseTypeCode"]
      self.IsFiltered:bool = obj["IsFiltered"]
      self.OprTypeCode:str = obj["OprTypeCode"]
      self.CashDeskID:str = obj["CashDeskID"]
      self.TIN:str = obj["TIN"]
      self.ReclassCodeID:str = obj["ReclassCodeID"]
      self.BitFlag:int = obj["BitFlag"]
      self.GLCntrlDescription:str = obj["GLCntrlDescription"]
      self.GLCntrlTypeDescription:str = obj["GLCntrlTypeDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_LangDescRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.TableName:str = obj["TableName"]
      """  Name of table that this data is related  """  
      self.LangNameID:str = obj["LangNameID"]
      """  Language ID  """  
      self.Key1:str = obj["Key1"]
      """  Contains values that represent the key1 to the foreign record that this record is related.  """  
      self.Key2:str = obj["Key2"]
      """  key2  of  the foreign record  """  
      self.Key3:str = obj["Key3"]
      """  key3 of the foreign record  """  
      self.Description:str = obj["Description"]
      """  Language Description  """  
      self.GlobalLangDesc:bool = obj["GlobalLangDesc"]
      """  Marks this LangDesc as global, available to be sent out to other companies.  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Disables this record from receiving global updates.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.LangNameIDDescription:str = obj["LangNameIDDescription"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PLSAFTCodeRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.RateCode:str = obj["RateCode"]
      """  RateCode  """  
      self.TaxCode:str = obj["TaxCode"]
      """  TaxCode  """  
      self.SAFTCode:str = obj["SAFTCode"]
      """  SAFTCode  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.CodeDesc:str = obj["CodeDesc"]
      self.LongDesc:str = obj["LongDesc"]
      self.TempSAFTCode:str = obj["TempSAFTCode"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_SalesTRCRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.TaxCode:str = obj["TaxCode"]
      """  Descriptive code assigned by user which uniquely identifies a Sales Tax master record.  Can't be blank. This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited.  """  
      self.RateCode:str = obj["RateCode"]
      """  Rate Code  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.DefaultRate:bool = obj["DefaultRate"]
      """  Default Rate  """  
      self.TextCode:str = obj["TextCode"]
      """  Legal Text code  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.AGAFIPCode:str = obj["AGAFIPCode"]
      """  AGAFIPCode  """  
      self.AGFEAFIPCode:str = obj["AGFEAFIPCode"]
      """  AGFEAFIPCode  """  
      self.AGPurchaseColNumber:int = obj["AGPurchaseColNumber"]
      """  AGPurchaseColNumber  """  
      self.AGSalesColNumber:int = obj["AGSalesColNumber"]
      """  AGSalesColNumber  """  
      self.BEIntracomCode:str = obj["BEIntracomCode"]
      """  Intracom Code (CSF Belgium)  """  
      self.JPConsumptionTax:bool = obj["JPConsumptionTax"]
      """  JPConsumptionTax  """  
      self.PLSAFTCode:str = obj["PLSAFTCode"]
      """  PLSAFTCode  """  
      self.CODIANCode:str = obj["CODIANCode"]
      """  CODIANCode  """  
      self.ExternalTaxCategory:str = obj["ExternalTaxCategory"]
      """  UNCL5305  """  
      self.FatherDeleted:bool = obj["FatherDeleted"]
      """  Indicate if is tring to be deleted from SalesTax  """  
      self.BitFlag:int = obj["BitFlag"]
      self.TaxTextDescription:str = obj["TaxTextDescription"]
      self.XbSystELIEinvoice:bool = obj["XbSystELIEinvoice"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_SalesTaxListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.TaxCode:str = obj["TaxCode"]
      """  Descriptive code assigned by user which uniquely identifies a Sales Tax master record.  Can't be blank. This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited.  """  
      self.Description:str = obj["Description"]
      """  Full description for a  Sales Tax master.  """  
      self.Manual:bool = obj["Manual"]
      """  Indicates if the tax calculations are to be performed manually.  This field is used as a default for the InvcTax.Manual field.  When this field is set in the InvcTax record the InvcTax.Reportable, InvcTax.TaxableAmt, and InvcTax.TaxAmount fields are enabled.  When it is NOT set these fields are DISABLED and the system will perform all of the Reportable, Taxable, and TaxAmount calculations automatically.  """  
      self.RoundDown:bool = obj["RoundDown"]
      """  Indicates if set to Yes that any decimal values of a penny/cent should be rounded down rather than rounded to nearest penny/cent.  """  
      self.Advanced:bool = obj["Advanced"]
      """  When checked the sales tax code will apply to advanced billing invoices, and will only apply to additional sums on final invoices.  """  
      self.TaxConnectCalc:bool = obj["TaxConnectCalc"]
      """  Indicates whether taxes related to this Sales Tax ID are calculated via Epicor Tax Connect interface. Default is No.  """  
      self.ETCJurisKey:str = obj["ETCJurisKey"]
      """  If this SalesTax id is used by TaxConnect, this is a string containing the data required to uniquely identify a specific taxing jurisdiction using the tax connect system data. It will be used to generate the ETCHash field. If multiple fields from the tax connect system are required to generate a unique key, they should be concatenated, separated by ?:?. For Avalara it will be the StateJurisCode+ ?:? + TaxDetail JurisCode + ?:? + TaxDetail JurisName returned by the GetTax function for each tax amount. Default is null.  """  
      self.ETCHash:int = obj["ETCHash"]
      """  If this SalesTax id is used by TaxConnect, this is the hash field to be used to cross reference the key fields provided by the tax connect service (stored in ETCJurisKey)  with the Epicor SalesTax id of this record in order to obtain the correct tax accrual GLs for the transaction. Default is null.  """  
      self.CollectionType:int = obj["CollectionType"]
      """  Collection Type  """  
      self.Timing:int = obj["Timing"]
      """  Timing of when to report taxes (default)  """  
      self.Algorithm:str = obj["Algorithm"]
      """  Algorithm  """  
      self.DiscountType:int = obj["DiscountType"]
      """  Discount Types, none, payment discount affect tax, terms discount affect tax  """  
      self.TaxJurisCode:str = obj["TaxJurisCode"]
      """  Tax Jurisdiction  """  
      self.RptCatCode:str = obj["RptCatCode"]
      """  Tax Report Category  """  
      self.TextCode:str = obj["TextCode"]
      """  Legal Text Code  """  
      self.InPrice:bool = obj["InPrice"]
      """  In Price  """  
      self.LglNumType:int = obj["LglNumType"]
      """  Tax Certificate Numbering method  """  
      self.LglNumSeq:int = obj["LglNumSeq"]
      """  Legal Number Sequence  """  
      self.RevRptCatCode:str = obj["RevRptCatCode"]
      """  Reverse Tax Report Category  """  
      self.ServiceTaxPoint:bool = obj["ServiceTaxPoint"]
      """  Intra-EU Service  """  
      self.Direct:str = obj["Direct"]
      """  Sales List Type Indicator  """  
      self.Triangulation:str = obj["Triangulation"]
      """  Sales List Type Indicator  """  
      self.GlobalSalesTax:bool = obj["GlobalSalesTax"]
      """  Marks this SalesTax as global, available to be sent out to other companies.  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Disables this record from receiving global updates.  """  
      self.InvoiceType:str = obj["InvoiceType"]
      """  Invoice Type: 0-No Vat Reporting, 1-Tax Invoice, 2-Duty-Free Invoice  """  
      self.InvMethod:str = obj["InvMethod"]
      """  Invoicing Method: 0-No VAT Reporting, 1-Paper Invoice, 2-eInvoice, 3-No Invoice  """  
      self.CustType:str = obj["CustType"]
      """  Customer Type: 0-No VAT Reporting, 1-Company Sales, 2-Personal Sales  """  
      self.RevType:str = obj["RevType"]
      """  Revenue Type: 0-No VAT Reporting, 1-Trading Revenue, 2-Non-Trading Revenue  """  
      self.IssueType:str = obj["IssueType"]
      """  Issue Type: 0-No VAT Reporting, 1-Normal Invoice, 2-Issued by Supplier  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.ParentJurisdiction:str = obj["ParentJurisdiction"]
      """  Parent Tax Id  """  
      self.EnableRevCharge:bool = obj["EnableRevCharge"]
      """  Flag to indicate if Reverse Charge should be enabled.  """  
      self.EnableTaxBox:bool = obj["EnableTaxBox"]
      """  Flag to indicate if Tax Box maintenance should be allowed.  """  
      self.mtlDescription:str = obj["mtlDescription"]
      """  Description of the record, translated in the selected language  """  
      self.mtlLangDesc:str = obj["mtlLangDesc"]
      """  Name of the selected language of Description  """  
      self.mtlLangId:str = obj["mtlLangId"]
      """  ID of the selected language  """  
      self.TaxAlgrmDescription:str = obj["TaxAlgrmDescription"]
      """  Description  """  
      self.TaxJurisDescription:str = obj["TaxJurisDescription"]
      """  Description  """  
      self.TaxRptCatDescription:str = obj["TaxRptCatDescription"]
      """  Description  """  
      self.TaxTextDescription:str = obj["TaxTextDescription"]
      """  Description  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_SalesTaxListTableset:
   def __init__(self, obj):
      self.SalesTaxList:list[Erp_Tablesets_SalesTaxListRow] = obj["SalesTaxList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_SalesTaxRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.TaxCode:str = obj["TaxCode"]
      """  Descriptive code assigned by user which uniquely identifies a Sales Tax master record.  Can't be blank. This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited.  """  
      self.Description:str = obj["Description"]
      """  Full description for a  Sales Tax master.  """  
      self.Manual:bool = obj["Manual"]
      """  Indicates if the tax calculations are to be performed manually.  This field is used as a default for the InvcTax.Manual field.  When this field is set in the InvcTax record the InvcTax.Reportable, InvcTax.TaxableAmt, and InvcTax.TaxAmount fields are enabled.  When it is NOT set these fields are DISABLED and the system will perform all of the Reportable, Taxable, and TaxAmount calculations automatically.  """  
      self.RoundDown:bool = obj["RoundDown"]
      """  Indicates if set to Yes that any decimal values of a penny/cent should be rounded down rather than rounded to nearest penny/cent.  """  
      self.Advanced:bool = obj["Advanced"]
      """  When checked the sales tax code will apply to advanced billing invoices, and will only apply to additional sums on final invoices.  """  
      self.TaxConnectCalc:bool = obj["TaxConnectCalc"]
      """  Indicates whether taxes related to this Sales Tax ID are calculated via Epicor Tax Connect interface. Default is No.  """  
      self.ETCJurisKey:str = obj["ETCJurisKey"]
      """  If this SalesTax id is used by TaxConnect, this is a string containing the data required to uniquely identify a specific taxing jurisdiction using the tax connect system data. It will be used to generate the ETCHash field. If multiple fields from the tax connect system are required to generate a unique key, they should be concatenated, separated by ?:?. For Avalara it will be the StateJurisCode+ ?:? + TaxDetail JurisCode + ?:? + TaxDetail JurisName returned by the GetTax function for each tax amount. Default is null.  """  
      self.ETCHash:int = obj["ETCHash"]
      """  If this SalesTax id is used by TaxConnect, this is the hash field to be used to cross reference the key fields provided by the tax connect service (stored in ETCJurisKey)  with the Epicor SalesTax id of this record in order to obtain the correct tax accrual GLs for the transaction. Default is null.  """  
      self.CollectionType:int = obj["CollectionType"]
      """  Collection Type  """  
      self.Timing:int = obj["Timing"]
      """  Timing of when to report taxes (default)  """  
      self.Algorithm:str = obj["Algorithm"]
      """  Algorithm  """  
      self.DiscountType:int = obj["DiscountType"]
      """  Discount Types, none, payment discount affect tax, terms discount affect tax  """  
      self.TaxJurisCode:str = obj["TaxJurisCode"]
      """  Tax Jurisdiction  """  
      self.RptCatCode:str = obj["RptCatCode"]
      """  Tax Report Category  """  
      self.TextCode:str = obj["TextCode"]
      """  Legal Text Code  """  
      self.InPrice:bool = obj["InPrice"]
      """  In Price  """  
      self.LglNumType:int = obj["LglNumType"]
      """  Tax Certificate Numbering method  """  
      self.LglNumSeq:int = obj["LglNumSeq"]
      """  Legal Number Sequence  """  
      self.RevRptCatCode:str = obj["RevRptCatCode"]
      """  Reverse Tax Report Category  """  
      self.ServiceTaxPoint:bool = obj["ServiceTaxPoint"]
      """  Intra-EU Service  """  
      self.Direct:str = obj["Direct"]
      """  Sales List Type Indicator  """  
      self.Triangulation:str = obj["Triangulation"]
      """  Sales List Type Indicator  """  
      self.GlobalSalesTax:bool = obj["GlobalSalesTax"]
      """  Marks this SalesTax as global, available to be sent out to other companies.  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Disables this record from receiving global updates.  """  
      self.InvoiceType:str = obj["InvoiceType"]
      """  Invoice Type: 0-No Vat Reporting, 1-Tax Invoice, 2-Duty-Free Invoice  """  
      self.InvMethod:str = obj["InvMethod"]
      """  Invoicing Method: 0-No VAT Reporting, 1-Paper Invoice, 2-eInvoice, 3-No Invoice  """  
      self.CustType:str = obj["CustType"]
      """  Customer Type: 0-No VAT Reporting, 1-Company Sales, 2-Personal Sales  """  
      self.RevType:str = obj["RevType"]
      """  Revenue Type: 0-No VAT Reporting, 1-Trading Revenue, 2-Non-Trading Revenue  """  
      self.IssueType:str = obj["IssueType"]
      """  Issue Type: 0-No VAT Reporting, 1-Normal Invoice, 2-Issued by Supplier  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.INIsCST:bool = obj["INIsCST"]
      """  INIsCST  """  
      self.AGAFIPCode:str = obj["AGAFIPCode"]
      """  AGAFIPCode  """  
      self.AGAFIPTaxRegCode:str = obj["AGAFIPTaxRegCode"]
      """  AGAFIPTaxRegCode  """  
      self.AGAFIPTaxRegDesc:str = obj["AGAFIPTaxRegDesc"]
      """  AGAFIPTaxRegDesc  """  
      self.AGMinimumByTax:bool = obj["AGMinimumByTax"]
      """  AGMinimumByTax  """  
      self.AGTaxableAmtType:str = obj["AGTaxableAmtType"]
      """  AGTaxableAmtType  """  
      self.AGWHHeader:str = obj["AGWHHeader"]
      """  AGWHHeader  """  
      self.IndirectTaxType:str = obj["IndirectTaxType"]
      """  IndirectTaxType  """  
      self.MXTaxCategory:str = obj["MXTaxCategory"]
      """  Mexico Localizaion field to store TaxType Category for Mexico  """  
      self.NOTaxCategory:str = obj["NOTaxCategory"]
      """  NOTaxCategory  """  
      self.PETranDocTypeID:str = obj["PETranDocTypeID"]
      """  PETranDocTypeID  """  
      self.PETaxOriginType:str = obj["PETaxOriginType"]
      """  PETaxOriginType  """  
      self.MXSATCode:str = obj["MXSATCode"]
      """  MXSATCode  """  
      self.PESUNATCode:str = obj["PESUNATCode"]
      """  PE SUNAT Code  """  
      self.PESUNATName:str = obj["PESUNATName"]
      """  PE SUNAT Name  """  
      self.PESUNATType:str = obj["PESUNATType"]
      """  PE SUNAT Type  """  
      self.PLSAFTCode:str = obj["PLSAFTCode"]
      """  PLSAFTCode  """  
      self.MXTaxType:str = obj["MXTaxType"]
      """  MXTaxType  """  
      self.MXTypeFactor:str = obj["MXTypeFactor"]
      """  MXTypeFactor  """  
      self.SendToFSA:bool = obj["SendToFSA"]
      """  Determines if the tax type has to be synchronized with Epicor FSA application.  """  
      self.TimingDepositAdvBilling:int = obj["TimingDepositAdvBilling"]
      """  Timing of when to report taxes (specific to Deposit Billing and Advanced Billing invoices)  """  
      self.EInvTaxCategory:str = obj["EInvTaxCategory"]
      """  E-Invoice Tax Category  """  
      self.PEISCCalcCode:str = obj["PEISCCalcCode"]
      """  PEISCCalcCode  """  
      self.PEAllowanceChargeReasonCode:str = obj["PEAllowanceChargeReasonCode"]
      """  PEAllowanceChargeReasonCode  """  
      self.ExternalTaxCategory:str = obj["ExternalTaxCategory"]
      """  Tax category; Country specific, e.g. ‘GST’ for ANZ. UNTDID 5153  """  
      self.AllowConfirmationTax:bool = obj["AllowConfirmationTax"]
      self.EnableRevCharge:bool = obj["EnableRevCharge"]
      """  Flag to indicate if Reverse Charge should be enabled.  """  
      self.EnableTaxBox:bool = obj["EnableTaxBox"]
      """  Flag to indicate if Tax Box maintenance should be allowed.  """  
      self.mtlDescription:str = obj["mtlDescription"]
      """  Description of the record, translated in the selected language  """  
      self.mtlLangDesc:str = obj["mtlLangDesc"]
      """  Name of the selected language of Description  """  
      self.mtlLangId:str = obj["mtlLangId"]
      """  ID of the selected language  """  
      self.ParentJurisdiction:str = obj["ParentJurisdiction"]
      """  Parent Tax Id  """  
      self.PEISCCalcCodeDesc:str = obj["PEISCCalcCodeDesc"]
      self.PESUNATCodeDesc:str = obj["PESUNATCodeDesc"]
      self.EnableChanges:bool = obj["EnableChanges"]
      """  Flag to indicate if the tax type is assigned to a tax liability.  """  
      self.PEAllowanceChargeReasonDesc:str = obj["PEAllowanceChargeReasonDesc"]
      """  Peru CSF: Allowance Change Reason Code description  """  
      self.BitFlag:int = obj["BitFlag"]
      self.CompanySendToFSA:bool = obj["CompanySendToFSA"]
      self.TaxAlgrmDescription:str = obj["TaxAlgrmDescription"]
      self.TaxJurisDescription:str = obj["TaxJurisDescription"]
      self.TaxRptCatDescription:str = obj["TaxRptCatDescription"]
      self.TaxTextDescription:str = obj["TaxTextDescription"]
      self.XbSystELIEinvoice:bool = obj["XbSystELIEinvoice"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_SalesTaxTableset:
   def __init__(self, obj):
      self.SalesTax:list[Erp_Tablesets_SalesTaxRow] = obj["SalesTax"]
      self.LangDesc:list[Erp_Tablesets_LangDescRow] = obj["LangDesc"]
      self.SalesTRC:list[Erp_Tablesets_SalesTRCRow] = obj["SalesTRC"]
      self.EntityGLC:list[Erp_Tablesets_EntityGLCRow] = obj["EntityGLC"]
      self.SalesTxc:list[Erp_Tablesets_SalesTxcRow] = obj["SalesTxc"]
      self.TaxBox:list[Erp_Tablesets_TaxBoxRow] = obj["TaxBox"]
      self.TaxRate:list[Erp_Tablesets_TaxRateRow] = obj["TaxRate"]
      self.EffRateEntityGLC:list[Erp_Tablesets_EffRateEntityGLCRow] = obj["EffRateEntityGLC"]
      self.TaxBoxEffRate:list[Erp_Tablesets_TaxBoxEffRateRow] = obj["TaxBoxEffRate"]
      self.TaxGRate:list[Erp_Tablesets_TaxGRateRow] = obj["TaxGRate"]
      self.PLSAFTCode:list[Erp_Tablesets_PLSAFTCodeRow] = obj["PLSAFTCode"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_SalesTxcRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.TaxCode:str = obj["TaxCode"]
      """  The TaxCode to which this record is related.  """  
      self.TaxCatID:str = obj["TaxCatID"]
      """  The TaxCatID which relates this record to the TaxCat record.  """  
      self.Reportable:bool = obj["Reportable"]
      """  Indicates that sales made of tax category are still reportable to the taxing jurisdiction as gross receipts even thou this category is  not  taxable.  """  
      self.RateCode:str = obj["RateCode"]
      """  Rate Code  """  
      self.ExemptType:int = obj["ExemptType"]
      """  Exemption Type  """  
      self.ExemptPercent:int = obj["ExemptPercent"]
      """  Exemption Percent  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.TaxCatIDDesc:str = obj["TaxCatIDDesc"]
      """  Tax category description  """  
      self.BitFlag:int = obj["BitFlag"]
      self.TaxCatIDDescription:str = obj["TaxCatIDDescription"]
      self.TaxCodeDescription:str = obj["TaxCodeDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_TaxBoxEffRateRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.TaxCode:str = obj["TaxCode"]
      """  TaxCode  """  
      self.BoxCode:str = obj["BoxCode"]
      """  BoxCode  """  
      self.SourceModule:str = obj["SourceModule"]
      """  SourceModule  """  
      self.AmountType:str = obj["AmountType"]
      """  AmountType  """  
      self.ECAcquisitionSeq:int = obj["ECAcquisitionSeq"]
      """  ECAcquisitionSeq  """  
      self.EffectiveFrom:str = obj["EffectiveFrom"]
      """  EffectiveFrom  """  
      self.BoxSign:str = obj["BoxSign"]
      """  BoxSign  """  
      self.RateCode:str = obj["RateCode"]
      """  RateCode  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.BoxCodeDescription:str = obj["BoxCodeDescription"]
      """  Box Code Description  """  
      self.EnableTaxBox:bool = obj["EnableTaxBox"]
      """  Flag to indicate if Tax Box maintenance should be allowed.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_TaxBoxRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.TaxCode:str = obj["TaxCode"]
      """  Descriptive code assigned by user which uniquely identifies a Sales Tax master record.  Can't be blank. This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited.  """  
      self.BoxCode:str = obj["BoxCode"]
      """  Tax Box Code.  """  
      self.SourceModule:str = obj["SourceModule"]
      """   Indicates the source module of the transaction for this tax box.
Possible values are: "AR" = from AR Invoice;  "AP" = from AP Invoice;  "ARCM" = from AR Credit Memo;  "APDM" = from AP Debit Memo.  """  
      self.AmountType:str = obj["AmountType"]
      """  The Amount type to be stored for this tax box.  The possible values are:  "Tax" = for Tax Amount; "Taxable" = for Taxable Amount.  """  
      self.ECAcquisitionSeq:int = obj["ECAcquisitionSeq"]
      """  Indicates if the tax line associated with this tax box is the Primary or Secondary line. This field corresponds to the ECAcquisitionSeq stored in the APInvTax to indicate the second reversing tax line.  Valid values are: 0 = Primary or Standard tax line;  1 = Secondary or Reversing tax line (only created if ECAcquisition or Reverse Charge apply)  """  
      self.BoxSign:str = obj["BoxSign"]
      """  Sign for box amount. + means add the taxable/tax amount to the (taxable/tax) box value; - means substract the taxable/tax amount from the (taxable/tax) box value.  """  
      self.RateCode:str = obj["RateCode"]
      """  Rate Code  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.EnableTaxBox:bool = obj["EnableTaxBox"]
      """  Flag to indicate if Tax Box maintenance should be allowed.  """  
      self.BoxCodeDescription:str = obj["BoxCodeDescription"]
      """  Box Code Description  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_TaxGRateRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.TaxCode:str = obj["TaxCode"]
      """  Descriptive code assigned by user which uniquely identifies a Sales Tax master record.  Can't be blank. This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited.  """  
      self.RateCode:str = obj["RateCode"]
      """  Tax Rate Code  """  
      self.EffectiveFrom:str = obj["EffectiveFrom"]
      """  First date tax rate is valid for  """  
      self.FromAmount:int = obj["FromAmount"]
      """  Minimum amount to apply tax to  """  
      self.TaxPercent:int = obj["TaxPercent"]
      """  Tax Percent to use  """  
      self.TaxAmount:int = obj["TaxAmount"]
      """  Fixed Tax Amount to apply  """  
      self.ReverseCharge:bool = obj["ReverseCharge"]
      """  Reverse Charge  """  
      self.TextCode:str = obj["TextCode"]
      """  Unique Identifier for Legal Text  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.ReverseAvail:bool = obj["ReverseAvail"]
      """  Flag to indicate if Reverse Charge check box is available to the user  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      self.BitFlag:int = obj["BitFlag"]
      self.TaxTextDescription:str = obj["TaxTextDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_TaxRateRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.TaxCode:str = obj["TaxCode"]
      """  Descriptive code assigned by user which uniquely identifies a Sales Tax master record.  Can't be blank. This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited.  """  
      self.RateCode:str = obj["RateCode"]
      """  Rate Code  """  
      self.EffectiveFrom:str = obj["EffectiveFrom"]
      """  First date tax rate is valid for  """  
      self.RateType:int = obj["RateType"]
      """  Percentage, Fixed Value or Graduated Rate  """  
      self.TaxPercent:int = obj["TaxPercent"]
      """  Tax Percent  """  
      self.TaxAmount:int = obj["TaxAmount"]
      """  Fixed Tax Amount  """  
      self.DeductPercent:int = obj["DeductPercent"]
      """  Deduction Percent  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  Currency Code  """  
      self.MinAmount:int = obj["MinAmount"]
      """  Minimum Amount  """  
      self.MaxAmount:int = obj["MaxAmount"]
      """  Maximum Amount  """  
      self.CentCode:str = obj["CentCode"]
      """  Cent Override Code  """  
      self.CompMethod:str = obj["CompMethod"]
      """  I - Document Level, L - Line Level  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.PEMinInvAmt:int = obj["PEMinInvAmt"]
      """  PEMinInvAmt  """  
      self.PEMinPayAmt:int = obj["PEMinPayAmt"]
      """  PEMinPayAmt  """  
      self.PEIncTaxAmt:bool = obj["PEIncTaxAmt"]
      """  PEIncTaxAmt  """  
      self.PEWHCurrencyCode:str = obj["PEWHCurrencyCode"]
      """  PEWHCurrencyCode  """  
      self.DisableDeduct:bool = obj["DisableDeduct"]
      """  Indicates if Deduct percent is not available for changes (always 100%)  """  
      self.DspTaxPercent:int = obj["DspTaxPercent"]
      """  PatchField for TaxPercent (using 3 decimals instead of 2)  """  
      self.EnableCopyTaxBoxFromLEffRate:bool = obj["EnableCopyTaxBoxFromLEffRate"]
      """  Enable copy Tax Boxes from Last Effective Rate  """  
      self.EnableCopyTaxBoxFromRates:bool = obj["EnableCopyTaxBoxFromRates"]
      """  Enable button copy Tax Boxes from Tax Rate Boxes  """  
      self.CollectionType:int = obj["CollectionType"]
      """  Like SalesTax.CollectionType - for technical purpose  """  
      self.BitFlag:int = obj["BitFlag"]
      self.CurrencyCurrName:str = obj["CurrencyCurrName"]
      self.CurrencyDocumentDesc:str = obj["CurrencyDocumentDesc"]
      self.CurrencyCurrDesc:str = obj["CurrencyCurrDesc"]
      self.CurrencyCurrencyID:str = obj["CurrencyCurrencyID"]
      self.CurrencyCurrSymbol:str = obj["CurrencyCurrSymbol"]
      self.TaxCentDescription:str = obj["TaxCentDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_UpdExtSalesTaxTableset:
   def __init__(self, obj):
      self.SalesTax:list[Erp_Tablesets_SalesTaxRow] = obj["SalesTax"]
      self.LangDesc:list[Erp_Tablesets_LangDescRow] = obj["LangDesc"]
      self.SalesTRC:list[Erp_Tablesets_SalesTRCRow] = obj["SalesTRC"]
      self.EntityGLC:list[Erp_Tablesets_EntityGLCRow] = obj["EntityGLC"]
      self.SalesTxc:list[Erp_Tablesets_SalesTxcRow] = obj["SalesTxc"]
      self.TaxBox:list[Erp_Tablesets_TaxBoxRow] = obj["TaxBox"]
      self.TaxRate:list[Erp_Tablesets_TaxRateRow] = obj["TaxRate"]
      self.EffRateEntityGLC:list[Erp_Tablesets_EffRateEntityGLCRow] = obj["EffRateEntityGLC"]
      self.TaxBoxEffRate:list[Erp_Tablesets_TaxBoxEffRateRow] = obj["TaxBoxEffRate"]
      self.TaxGRate:list[Erp_Tablesets_TaxGRateRow] = obj["TaxGRate"]
      self.PLSAFTCode:list[Erp_Tablesets_PLSAFTCodeRow] = obj["PLSAFTCode"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetByID_input:
   """ Required : 
   taxCode
   """  
   def __init__(self, obj):
      self.taxCode:str = obj["taxCode"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_SalesTaxTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_SalesTaxTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_SalesTaxTableset] = obj["returnObj"]
      pass

class GetCollectionDataForCombo_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

class GetDiscountTypes_input:
   """ Required : 
   collectionType
   """  
   def __init__(self, obj):
      self.collectionType:int = obj["collectionType"]
      pass

class GetDiscountTypes_output:
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
      self.returnObj:list[Erp_Tablesets_SalesTaxListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewEffRateEntityGLCOver_input:
   """ Required : 
   ds
   taxCode
   rateCode
   effectiveFrom
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_SalesTaxTableset] = obj["ds"]
      self.taxCode:str = obj["taxCode"]
      """  Tax Code of Effective Rate.  """  
      self.rateCode:str = obj["rateCode"]
      """  Rate Code of Effective Rate.  """  
      self.effectiveFrom:str = obj["effectiveFrom"]
      """  EffectiveFrom date of Effective Rate.  """  
      pass

class GetNewEffRateEntityGLCOver_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_SalesTaxTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewEffRateEntityGLC_input:
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
      self.ds:list[Erp_Tablesets_SalesTaxTableset] = obj["ds"]
      self.relatedToFile:str = obj["relatedToFile"]
      self.key1:str = obj["key1"]
      self.key2:str = obj["key2"]
      self.key3:str = obj["key3"]
      self.key4:str = obj["key4"]
      self.key5:str = obj["key5"]
      self.key6:str = obj["key6"]
      pass

class GetNewEffRateEntityGLC_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_SalesTaxTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewEntityGLC_input:
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
      self.ds:list[Erp_Tablesets_SalesTaxTableset] = obj["ds"]
      self.relatedToFile:str = obj["relatedToFile"]
      self.key1:str = obj["key1"]
      self.key2:str = obj["key2"]
      self.key3:str = obj["key3"]
      self.key4:str = obj["key4"]
      self.key5:str = obj["key5"]
      self.key6:str = obj["key6"]
      pass

class GetNewEntityGLC_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_SalesTaxTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewLangDesc_input:
   """ Required : 
   ds
   tableName
   key1
   key2
   key3
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_SalesTaxTableset] = obj["ds"]
      self.tableName:str = obj["tableName"]
      self.key1:str = obj["key1"]
      self.key2:str = obj["key2"]
      self.key3:str = obj["key3"]
      pass

class GetNewLangDesc_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_SalesTaxTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewPLSAFTCode_input:
   """ Required : 
   ds
   rateCode
   taxCode
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_SalesTaxTableset] = obj["ds"]
      self.rateCode:str = obj["rateCode"]
      self.taxCode:str = obj["taxCode"]
      pass

class GetNewPLSAFTCode_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_SalesTaxTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewSalesTRC_input:
   """ Required : 
   ds
   taxCode
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_SalesTaxTableset] = obj["ds"]
      self.taxCode:str = obj["taxCode"]
      pass

class GetNewSalesTRC_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_SalesTaxTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewSalesTax_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_SalesTaxTableset] = obj["ds"]
      pass

class GetNewSalesTax_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_SalesTaxTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewSalesTxc_input:
   """ Required : 
   ds
   taxCode
   rateCode
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_SalesTaxTableset] = obj["ds"]
      self.taxCode:str = obj["taxCode"]
      self.rateCode:str = obj["rateCode"]
      pass

class GetNewSalesTxc_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_SalesTaxTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewTaxBoxEffRateOver_input:
   """ Required : 
   ds
   taxCode
   rateCode
   effectiveFrom
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_SalesTaxTableset] = obj["ds"]
      self.taxCode:str = obj["taxCode"]
      self.rateCode:str = obj["rateCode"]
      self.effectiveFrom:str = obj["effectiveFrom"]
      pass

class GetNewTaxBoxEffRateOver_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_SalesTaxTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewTaxBoxEffRate_input:
   """ Required : 
   ds
   taxCode
   rateCode
   boxCode
   sourceModule
   amountType
   ecAcquisitionSeq
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_SalesTaxTableset] = obj["ds"]
      self.taxCode:str = obj["taxCode"]
      self.rateCode:str = obj["rateCode"]
      self.boxCode:str = obj["boxCode"]
      self.sourceModule:str = obj["sourceModule"]
      self.amountType:str = obj["amountType"]
      self.ecAcquisitionSeq:int = obj["ecAcquisitionSeq"]
      pass

class GetNewTaxBoxEffRate_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_SalesTaxTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewTaxBox_input:
   """ Required : 
   ds
   taxCode
   rateCode
   boxCode
   sourceModule
   amountType
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_SalesTaxTableset] = obj["ds"]
      self.taxCode:str = obj["taxCode"]
      self.rateCode:str = obj["rateCode"]
      self.boxCode:str = obj["boxCode"]
      self.sourceModule:str = obj["sourceModule"]
      self.amountType:str = obj["amountType"]
      pass

class GetNewTaxBox_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_SalesTaxTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewTaxGRate_input:
   """ Required : 
   ds
   taxCode
   rateCode
   effectiveFrom
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_SalesTaxTableset] = obj["ds"]
      self.taxCode:str = obj["taxCode"]
      self.rateCode:str = obj["rateCode"]
      self.effectiveFrom:str = obj["effectiveFrom"]
      pass

class GetNewTaxGRate_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_SalesTaxTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewTaxRate_input:
   """ Required : 
   ds
   taxCode
   rateCode
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_SalesTaxTableset] = obj["ds"]
      self.taxCode:str = obj["taxCode"]
      self.rateCode:str = obj["rateCode"]
      pass

class GetNewTaxRate_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_SalesTaxTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNumberingValues_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

class GetRateTypes_input:
   """ Required : 
   collectionType
   """  
   def __init__(self, obj):
      self.collectionType:int = obj["collectionType"]
      """  SalesTax.CollectionType  """  
      pass

class GetRateTypes_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

class GetRows_input:
   """ Required : 
   whereClauseSalesTax
   whereClauseLangDesc
   whereClauseSalesTRC
   whereClauseEntityGLC
   whereClauseSalesTxc
   whereClauseTaxBox
   whereClauseTaxRate
   whereClauseEffRateEntityGLC
   whereClauseTaxBoxEffRate
   whereClauseTaxGRate
   whereClausePLSAFTCode
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseSalesTax:str = obj["whereClauseSalesTax"]
      self.whereClauseLangDesc:str = obj["whereClauseLangDesc"]
      self.whereClauseSalesTRC:str = obj["whereClauseSalesTRC"]
      self.whereClauseEntityGLC:str = obj["whereClauseEntityGLC"]
      self.whereClauseSalesTxc:str = obj["whereClauseSalesTxc"]
      self.whereClauseTaxBox:str = obj["whereClauseTaxBox"]
      self.whereClauseTaxRate:str = obj["whereClauseTaxRate"]
      self.whereClauseEffRateEntityGLC:str = obj["whereClauseEffRateEntityGLC"]
      self.whereClauseTaxBoxEffRate:str = obj["whereClauseTaxBoxEffRate"]
      self.whereClauseTaxGRate:str = obj["whereClauseTaxGRate"]
      self.whereClausePLSAFTCode:str = obj["whereClausePLSAFTCode"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_SalesTaxTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetTimingDataForCombo_input:
   """ Required : 
   collectionType
   """  
   def __init__(self, obj):
      self.collectionType:int = obj["collectionType"]
      pass

class GetTimingDataForCombo_output:
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

class LookupPLSAFTCode_input:
   """ Required : 
   code
   rateCode
   taxCode
   ds
   """  
   def __init__(self, obj):
      self.code:str = obj["code"]
      self.rateCode:str = obj["rateCode"]
      self.taxCode:str = obj["taxCode"]
      self.ds:list[Erp_Tablesets_SalesTaxTableset] = obj["ds"]
      pass

class LookupPLSAFTCode_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_SalesTaxTableset] = obj["ds"]
      pass

      """  output parameters  """  

class PEChangeType_input:
   """ Required : 
   value
   ds
   """  
   def __init__(self, obj):
      self.value:str = obj["value"]
      """  value  """  
      self.ds:list[Erp_Tablesets_SalesTaxTableset] = obj["ds"]
      pass

class PEChangeType_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_SalesTaxTableset] = obj["ds"]
      pass

      """  output parameters  """  

class PEChangeUDCode_input:
   """ Required : 
   codeType
   ds
   """  
   def __init__(self, obj):
      self.codeType:str = obj["codeType"]
      """  User code  """  
      self.ds:list[Erp_Tablesets_SalesTaxTableset] = obj["ds"]
      pass

class PEChangeUDCode_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_SalesTaxTableset] = obj["ds"]
      pass

      """  output parameters  """  

class RemovePLSAFTCode_input:
   """ Required : 
   rateCode
   taxCode
   """  
   def __init__(self, obj):
      self.rateCode:str = obj["rateCode"]
      self.taxCode:str = obj["taxCode"]
      pass

class RemovePLSAFTCode_output:
   def __init__(self, obj):
      pass

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtSalesTaxTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtSalesTaxTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class UpdatePLSAFTCode_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_SalesTaxTableset] = obj["ds"]
      pass

class UpdatePLSAFTCode_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_SalesTaxTableset] = obj["ds"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_SalesTaxTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_SalesTaxTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ValidateEffectiveDate_input:
   """ Required : 
   sTaxCode
   sRateCode
   dEffectiveDate
   """  
   def __init__(self, obj):
      self.sTaxCode:str = obj["sTaxCode"]
      """  Tax code  """  
      self.sRateCode:str = obj["sRateCode"]
      """  Rate Code  """  
      self.dEffectiveDate:str = obj["dEffectiveDate"]
      """  Returns VendorNum as a character  """  
      pass

class ValidateEffectiveDate_output:
   def __init__(self, obj):
      pass

