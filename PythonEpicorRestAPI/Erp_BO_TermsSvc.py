import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.TermsSvc
# Description: Add your summary for this object here
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TermsSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TermsSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_Terms(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get Terms items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_Terms
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.TermsRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TermsSvc/Terms",headers=creds) as resp:
           return await resp.json()

async def post_Terms(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_Terms
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.TermsRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.TermsRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TermsSvc/Terms", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_Terms_Company_TermsCode(Company, TermsCode, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the Term item
   Description: Calls GetByID to retrieve the Term item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_Term
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TermsCode: Desc: TermsCode   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.TermsRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TermsSvc/Terms(" + Company + "," + TermsCode + ")",headers=creds) as resp:
           return await resp.json()

async def patch_Terms_Company_TermsCode(Company, TermsCode, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update Term for the service
   Description: Calls UpdateExt to update Term. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_Term
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TermsCode: Desc: TermsCode   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.TermsRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.TermsSvc/Terms(" + Company + "," + TermsCode + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_Terms_Company_TermsCode(Company, TermsCode, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete Term item
   Description: Call UpdateExt to delete Term item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_Term
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TermsCode: Desc: TermsCode   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.TermsSvc/Terms(" + Company + "," + TermsCode + ")",headers=creds) as resp:
           return await resp.json()

async def get_Terms_Company_TermsCode_LangDescs(Company, TermsCode, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get LangDescs items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_LangDescs1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TermsCode: Desc: TermsCode   Required: True   Allow empty value : True
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TermsSvc/Terms(" + Company + "," + TermsCode + ")/LangDescs",headers=creds) as resp:
           return await resp.json()

async def get_Terms_Company_TermsCode_LangDescs_Company_TableName_Key1_Key2_Key3_LangNameID(Company, TermsCode, TableName, Key1, Key2, Key3, LangNameID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the LangDesc item
   Description: Calls GetByID to retrieve the LangDesc item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_LangDesc1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TermsCode: Desc: TermsCode   Required: True   Allow empty value : True
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TermsSvc/Terms(" + Company + "," + TermsCode + ")/LangDescs(" + Company + "," + TableName + "," + Key1 + "," + Key2 + "," + Key3 + "," + LangNameID + ")",headers=creds) as resp:
           return await resp.json()

async def get_Terms_Company_TermsCode_TermsDtls(Company, TermsCode, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get TermsDtls items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_TermsDtls1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TermsCode: Desc: TermsCode   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.TermsDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TermsSvc/Terms(" + Company + "," + TermsCode + ")/TermsDtls",headers=creds) as resp:
           return await resp.json()

async def get_Terms_Company_TermsCode_TermsDtls_Company_TermsCode_TermsSeq(Company, TermsCode, TermsSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the TermsDtl item
   Description: Calls GetByID to retrieve the TermsDtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_TermsDtl1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TermsCode: Desc: TermsCode   Required: True   Allow empty value : True
      :param TermsSeq: Desc: TermsSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.TermsDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TermsSvc/Terms(" + Company + "," + TermsCode + ")/TermsDtls(" + Company + "," + TermsCode + "," + TermsSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_Terms_Company_TermsCode_TermsScheds(Company, TermsCode, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get TermsScheds items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_TermsScheds1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TermsCode: Desc: TermsCode   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.TermsSchedRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TermsSvc/Terms(" + Company + "," + TermsCode + ")/TermsScheds",headers=creds) as resp:
           return await resp.json()

async def get_Terms_Company_TermsCode_TermsScheds_Company_TermsCode_PaySeq(Company, TermsCode, PaySeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the TermsSched item
   Description: Calls GetByID to retrieve the TermsSched item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_TermsSched1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TermsCode: Desc: TermsCode   Required: True   Allow empty value : True
      :param PaySeq: Desc: PaySeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.TermsSchedRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TermsSvc/Terms(" + Company + "," + TermsCode + ")/TermsScheds(" + Company + "," + TermsCode + "," + PaySeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_Terms_Company_TermsCode_TermsAttches(Company, TermsCode, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get TermsAttches items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_TermsAttches1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TermsCode: Desc: TermsCode   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.TermsAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TermsSvc/Terms(" + Company + "," + TermsCode + ")/TermsAttches",headers=creds) as resp:
           return await resp.json()

async def get_Terms_Company_TermsCode_TermsAttches_Company_TermsCode_DrawingSeq(Company, TermsCode, DrawingSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the TermsAttch item
   Description: Calls GetByID to retrieve the TermsAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_TermsAttch1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TermsCode: Desc: TermsCode   Required: True   Allow empty value : True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.TermsAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TermsSvc/Terms(" + Company + "," + TermsCode + ")/TermsAttches(" + Company + "," + TermsCode + "," + DrawingSeq + ")",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TermsSvc/LangDescs",headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TermsSvc/LangDescs", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TermsSvc/LangDescs(" + Company + "," + TableName + "," + Key1 + "," + Key2 + "," + Key3 + "," + LangNameID + ")",headers=creds) as resp:
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
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.TermsSvc/LangDescs(" + Company + "," + TableName + "," + Key1 + "," + Key2 + "," + Key3 + "," + LangNameID + ")", json=requestBody,headers=creds) as resp:
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.TermsSvc/LangDescs(" + Company + "," + TableName + "," + Key1 + "," + Key2 + "," + Key3 + "," + LangNameID + ")",headers=creds) as resp:
           return await resp.json()

async def get_TermsDtls(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get TermsDtls items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_TermsDtls
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.TermsDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TermsSvc/TermsDtls",headers=creds) as resp:
           return await resp.json()

async def post_TermsDtls(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_TermsDtls
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.TermsDtlRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.TermsDtlRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TermsSvc/TermsDtls", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_TermsDtls_Company_TermsCode_TermsSeq(Company, TermsCode, TermsSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the TermsDtl item
   Description: Calls GetByID to retrieve the TermsDtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_TermsDtl
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TermsCode: Desc: TermsCode   Required: True   Allow empty value : True
      :param TermsSeq: Desc: TermsSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.TermsDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TermsSvc/TermsDtls(" + Company + "," + TermsCode + "," + TermsSeq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_TermsDtls_Company_TermsCode_TermsSeq(Company, TermsCode, TermsSeq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update TermsDtl for the service
   Description: Calls UpdateExt to update TermsDtl. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_TermsDtl
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TermsCode: Desc: TermsCode   Required: True   Allow empty value : True
      :param TermsSeq: Desc: TermsSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.TermsDtlRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.TermsSvc/TermsDtls(" + Company + "," + TermsCode + "," + TermsSeq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_TermsDtls_Company_TermsCode_TermsSeq(Company, TermsCode, TermsSeq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete TermsDtl item
   Description: Call UpdateExt to delete TermsDtl item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_TermsDtl
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TermsCode: Desc: TermsCode   Required: True   Allow empty value : True
      :param TermsSeq: Desc: TermsSeq   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.TermsSvc/TermsDtls(" + Company + "," + TermsCode + "," + TermsSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_TermsScheds(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get TermsScheds items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_TermsScheds
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.TermsSchedRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TermsSvc/TermsScheds",headers=creds) as resp:
           return await resp.json()

async def post_TermsScheds(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_TermsScheds
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.TermsSchedRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.TermsSchedRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TermsSvc/TermsScheds", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_TermsScheds_Company_TermsCode_PaySeq(Company, TermsCode, PaySeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the TermsSched item
   Description: Calls GetByID to retrieve the TermsSched item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_TermsSched
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TermsCode: Desc: TermsCode   Required: True   Allow empty value : True
      :param PaySeq: Desc: PaySeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.TermsSchedRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TermsSvc/TermsScheds(" + Company + "," + TermsCode + "," + PaySeq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_TermsScheds_Company_TermsCode_PaySeq(Company, TermsCode, PaySeq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update TermsSched for the service
   Description: Calls UpdateExt to update TermsSched. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_TermsSched
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TermsCode: Desc: TermsCode   Required: True   Allow empty value : True
      :param PaySeq: Desc: PaySeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.TermsSchedRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.TermsSvc/TermsScheds(" + Company + "," + TermsCode + "," + PaySeq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_TermsScheds_Company_TermsCode_PaySeq(Company, TermsCode, PaySeq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete TermsSched item
   Description: Call UpdateExt to delete TermsSched item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_TermsSched
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TermsCode: Desc: TermsCode   Required: True   Allow empty value : True
      :param PaySeq: Desc: PaySeq   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.TermsSvc/TermsScheds(" + Company + "," + TermsCode + "," + PaySeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_TermsAttches(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get TermsAttches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_TermsAttches
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.TermsAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TermsSvc/TermsAttches",headers=creds) as resp:
           return await resp.json()

async def post_TermsAttches(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_TermsAttches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.TermsAttchRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.TermsAttchRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TermsSvc/TermsAttches", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_TermsAttches_Company_TermsCode_DrawingSeq(Company, TermsCode, DrawingSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the TermsAttch item
   Description: Calls GetByID to retrieve the TermsAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_TermsAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TermsCode: Desc: TermsCode   Required: True   Allow empty value : True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.TermsAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TermsSvc/TermsAttches(" + Company + "," + TermsCode + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_TermsAttches_Company_TermsCode_DrawingSeq(Company, TermsCode, DrawingSeq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update TermsAttch for the service
   Description: Calls UpdateExt to update TermsAttch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_TermsAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TermsCode: Desc: TermsCode   Required: True   Allow empty value : True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.TermsAttchRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.TermsSvc/TermsAttches(" + Company + "," + TermsCode + "," + DrawingSeq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_TermsAttches_Company_TermsCode_DrawingSeq(Company, TermsCode, DrawingSeq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete TermsAttch item
   Description: Call UpdateExt to delete TermsAttch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_TermsAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TermsCode: Desc: TermsCode   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.TermsSvc/TermsAttches(" + Company + "," + TermsCode + "," + DrawingSeq + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.TermsListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TermsSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseTerms, whereClauseTermsAttch, whereClauseLangDesc, whereClauseTermsDtl, whereClauseTermsSched, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClauseTerms=" + whereClauseTerms
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseTermsAttch=" + whereClauseTermsAttch
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
   params += "whereClauseTermsDtl=" + whereClauseTermsDtl
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseTermsSched=" + whereClauseTermsSched
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TermsSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(termsCode, epicorHeaders = None):
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
   params += "termsCode=" + termsCode

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TermsSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_OnChangingDisDays(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangingDisDays
   OperationID: OnChangingDisDays
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangingDisDays_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangingDisDays_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TermsSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangingDisPercent(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangingDisPercent
   OperationID: OnChangingDisPercent
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangingDisPercent_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangingDisPercent_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TermsSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangingNumOfDays(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangingNumOfDays
   OperationID: OnChangingNumOfDays
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangingNumOfDays_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangingNumOfDays_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TermsSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangingNumOfMonths(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangingNumOfMonths
   OperationID: OnChangingNumOfMonths
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangingNumOfMonths_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangingNumOfMonths_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TermsSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangingTermDueOnDay(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangingTermDueOnDay
   OperationID: OnChangingTermDueOnDay
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangingTermDueOnDay_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangingTermDueOnDay_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TermsSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetTermsSched(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetTermsSched
   OperationID: GetTermsSched
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetTermsSched_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetTermsSched_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TermsSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnTermsSchedPercentageUpdate(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnTermsSchedPercentageUpdate
   Description: This methods should be called when the Percentage value of payment has been modified or when a Payment is added using the standard GetNew funtionality.
   OperationID: OnTermsSchedPercentageUpdate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnTermsSchedPercentageUpdate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnTermsSchedPercentageUpdate_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TermsSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidateDiscountPercent(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateDiscountPercent
   Description: This method will check if current discount percent is less or greater than previous or next discounts and send a warning message.
   OperationID: ValidateDiscountPercent
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateDiscountPercent_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateDiscountPercent_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TermsSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewTerms(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewTerms
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewTerms
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewTerms_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewTerms_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TermsSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewTermsAttch(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewTermsAttch
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewTermsAttch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewTermsAttch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewTermsAttch_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TermsSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TermsSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewTermsDtl(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewTermsDtl
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewTermsDtl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewTermsDtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewTermsDtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TermsSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewTermsSched(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewTermsSched
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewTermsSched
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewTermsSched_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewTermsSched_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TermsSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TermsSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TermsSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TermsSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TermsSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TermsSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TermsSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LangDescRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_LangDescRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TermsAttchRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_TermsAttchRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TermsDtlRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_TermsDtlRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TermsListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_TermsListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TermsRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_TermsRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TermsSchedRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_TermsSchedRow] = obj["value"]
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

class Erp_Tablesets_TermsAttchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.TermsCode:str = obj["TermsCode"]
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

class Erp_Tablesets_TermsDtlRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.TermsCode:str = obj["TermsCode"]
      """  Unique identifier of the terms assigned by the user.  """  
      self.TermsSeq:int = obj["TermsSeq"]
      """  Sequence Counter to allow multiple Discounts  """  
      self.DueOnDay:int = obj["DueOnDay"]
      """  Used for Discount Type (Day of Months)  """  
      self.DiscountPercent:int = obj["DiscountPercent"]
      """   The discount percentage given for prompt payment of an invoice.
Invoice printing uses this value to calculate a prompt payment discount amount.  """  
      self.NumberOfMonths:int = obj["NumberOfMonths"]
      """  Used for Terms Type (X Month Y Days)  """  
      self.NumberOfDays:int = obj["NumberOfDays"]
      """  Used for Terms Type (X Months + Y Days)  """  
      self.MinimumDays:int = obj["MinimumDays"]
      """  Used for Disc Type (Days of Month)  """  
      self.GlobalTermsDtl:bool = obj["GlobalTermsDtl"]
      """  Marks this TermsDtl as global, available to be sent out to other companies.  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Disables this record from receiving global updates.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_TermsListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.TermsCode:str = obj["TermsCode"]
      """  Unique identifier of the terms assigned by the user.  """  
      self.SysDefault:bool = obj["SysDefault"]
      """  System Default Term  """  
      self.TermsType:str = obj["TermsType"]
      """  This field defines the type of the term  """  
      self.Description:str = obj["Description"]
      """  Full description of the terms which prints on sales orders and invoices.  """  
      self.NumberOfPayments:int = obj["NumberOfPayments"]
      """  Defines the number of installment payments that will be made for invoices using this specific terms. Invoicing will generate due dates and disburse the invoice total into equal corresponding amounts based on this value.  """  
      self.NumberOfDays:int = obj["NumberOfDays"]
      """  Used for Terms Type (X Months + Y Days)  """  
      self.MinimumDays:int = obj["MinimumDays"]
      """  Used for Terms Type (Days of Month)  """  
      self.DueOnDay:int = obj["DueOnDay"]
      """  Used for Terms Type (Day of Months)  """  
      self.NumberOfMonths:int = obj["NumberOfMonths"]
      """  Used for Terms Type (X Months + Y Days)  """  
      self.DiscountType:str = obj["DiscountType"]
      """  This field defines the type of the Discount  """  
      self.PartPayment:bool = obj["PartPayment"]
      """  Field to define when apply the discount percentage, can be when invoice is paid in full or Cash amount  """  
      self.ReqLOC:bool = obj["ReqLOC"]
      """  Require Letter of Credit.  """  
      self.GlobalTerms:bool = obj["GlobalTerms"]
      """  Marks this Terms as global, available to be sent out to other companies.  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Disables this record from receiving global updates.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.SystemDefault:bool = obj["SystemDefault"]
      """  Indicates if this terms is the system default  """  
      self.MonthlyDueDay:int = obj["MonthlyDueDay"]
      self.MonthlyOffset:int = obj["MonthlyOffset"]
      self.NonMonthlyDueDay:int = obj["NonMonthlyDueDay"]
      self.IsDefault:bool = obj["IsDefault"]
      """  Indicate if the term is default  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_TermsRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.TermsCode:str = obj["TermsCode"]
      """  Unique identifier of the terms assigned by the user.  """  
      self.SysDefault:bool = obj["SysDefault"]
      """  System Default Term  """  
      self.TermsType:str = obj["TermsType"]
      """  This field defines the type of the term  """  
      self.Description:str = obj["Description"]
      """  Full description of the terms which prints on sales orders and invoices.  """  
      self.NumberOfPayments:int = obj["NumberOfPayments"]
      """  Defines the number of installment payments that will be made for invoices using this specific terms. Invoicing will generate due dates and disburse the invoice total into equal corresponding amounts based on this value.  """  
      self.NumberOfDays:int = obj["NumberOfDays"]
      """  Used for Terms Type (X Months + Y Days)  """  
      self.MinimumDays:int = obj["MinimumDays"]
      """  Used for Terms Type (Days of Month)  """  
      self.DueOnDay:int = obj["DueOnDay"]
      """  Used for Terms Type (Day of Months)  """  
      self.NumberOfMonths:int = obj["NumberOfMonths"]
      """  Used for Terms Type (X Months + Y Days)  """  
      self.DiscountType:str = obj["DiscountType"]
      """  This field defines the type of the Discount  """  
      self.PartPayment:bool = obj["PartPayment"]
      """  Field to define when apply the discount percentage, can be when invoice is paid in full or Cash amount  """  
      self.ReqLOC:bool = obj["ReqLOC"]
      """  Require Letter of Credit.  """  
      self.GlobalTerms:bool = obj["GlobalTerms"]
      """  Marks this Terms as global, available to be sent out to other companies.  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Disables this record from receiving global updates.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.COIFRSCalculation:bool = obj["COIFRSCalculation"]
      """  COIFRSCalculation  """  
      self.COIFRSNumberOfPeriods:int = obj["COIFRSNumberOfPeriods"]
      """  COIFRSNumberOfPeriods  """  
      self.SystemDefault:bool = obj["SystemDefault"]
      """  Indicates if this terms is the system default  """  
      self.MonthlyDueDay:int = obj["MonthlyDueDay"]
      self.MonthlyOffset:int = obj["MonthlyOffset"]
      self.NonMonthlyDueDay:int = obj["NonMonthlyDueDay"]
      self.IsDefault:bool = obj["IsDefault"]
      """  Indicate if the term is default  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_TermsSchedRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.TermsCode:str = obj["TermsCode"]
      """  Unique identifier of the terms assigned by the user.  """  
      self.PaySeq:int = obj["PaySeq"]
      """  Specifies the number of payment of the Payment Schedule. This is an auto-generated sequence number.  """  
      self.PayDays:int = obj["PayDays"]
      """  Specifies the number of days for the payment to be paid. This is used to calculate Due Date in Invoice Payment Schedule.  """  
      self.PayPercent:int = obj["PayPercent"]
      """  Specifies the percent of the payment to be paid. This is used to calculate amount to be paid per payment in Sales Order and Invoice Payment Sechedule.  """  
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
   termsCode
   """  
   def __init__(self, obj):
      self.termsCode:str = obj["termsCode"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
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

class Erp_Tablesets_TermsAttchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.TermsCode:str = obj["TermsCode"]
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

class Erp_Tablesets_TermsDtlRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.TermsCode:str = obj["TermsCode"]
      """  Unique identifier of the terms assigned by the user.  """  
      self.TermsSeq:int = obj["TermsSeq"]
      """  Sequence Counter to allow multiple Discounts  """  
      self.DueOnDay:int = obj["DueOnDay"]
      """  Used for Discount Type (Day of Months)  """  
      self.DiscountPercent:int = obj["DiscountPercent"]
      """   The discount percentage given for prompt payment of an invoice.
Invoice printing uses this value to calculate a prompt payment discount amount.  """  
      self.NumberOfMonths:int = obj["NumberOfMonths"]
      """  Used for Terms Type (X Month Y Days)  """  
      self.NumberOfDays:int = obj["NumberOfDays"]
      """  Used for Terms Type (X Months + Y Days)  """  
      self.MinimumDays:int = obj["MinimumDays"]
      """  Used for Disc Type (Days of Month)  """  
      self.GlobalTermsDtl:bool = obj["GlobalTermsDtl"]
      """  Marks this TermsDtl as global, available to be sent out to other companies.  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Disables this record from receiving global updates.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_TermsListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.TermsCode:str = obj["TermsCode"]
      """  Unique identifier of the terms assigned by the user.  """  
      self.SysDefault:bool = obj["SysDefault"]
      """  System Default Term  """  
      self.TermsType:str = obj["TermsType"]
      """  This field defines the type of the term  """  
      self.Description:str = obj["Description"]
      """  Full description of the terms which prints on sales orders and invoices.  """  
      self.NumberOfPayments:int = obj["NumberOfPayments"]
      """  Defines the number of installment payments that will be made for invoices using this specific terms. Invoicing will generate due dates and disburse the invoice total into equal corresponding amounts based on this value.  """  
      self.NumberOfDays:int = obj["NumberOfDays"]
      """  Used for Terms Type (X Months + Y Days)  """  
      self.MinimumDays:int = obj["MinimumDays"]
      """  Used for Terms Type (Days of Month)  """  
      self.DueOnDay:int = obj["DueOnDay"]
      """  Used for Terms Type (Day of Months)  """  
      self.NumberOfMonths:int = obj["NumberOfMonths"]
      """  Used for Terms Type (X Months + Y Days)  """  
      self.DiscountType:str = obj["DiscountType"]
      """  This field defines the type of the Discount  """  
      self.PartPayment:bool = obj["PartPayment"]
      """  Field to define when apply the discount percentage, can be when invoice is paid in full or Cash amount  """  
      self.ReqLOC:bool = obj["ReqLOC"]
      """  Require Letter of Credit.  """  
      self.GlobalTerms:bool = obj["GlobalTerms"]
      """  Marks this Terms as global, available to be sent out to other companies.  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Disables this record from receiving global updates.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.SystemDefault:bool = obj["SystemDefault"]
      """  Indicates if this terms is the system default  """  
      self.MonthlyDueDay:int = obj["MonthlyDueDay"]
      self.MonthlyOffset:int = obj["MonthlyOffset"]
      self.NonMonthlyDueDay:int = obj["NonMonthlyDueDay"]
      self.IsDefault:bool = obj["IsDefault"]
      """  Indicate if the term is default  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_TermsListTableset:
   def __init__(self, obj):
      self.TermsList:list[Erp_Tablesets_TermsListRow] = obj["TermsList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_TermsRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.TermsCode:str = obj["TermsCode"]
      """  Unique identifier of the terms assigned by the user.  """  
      self.SysDefault:bool = obj["SysDefault"]
      """  System Default Term  """  
      self.TermsType:str = obj["TermsType"]
      """  This field defines the type of the term  """  
      self.Description:str = obj["Description"]
      """  Full description of the terms which prints on sales orders and invoices.  """  
      self.NumberOfPayments:int = obj["NumberOfPayments"]
      """  Defines the number of installment payments that will be made for invoices using this specific terms. Invoicing will generate due dates and disburse the invoice total into equal corresponding amounts based on this value.  """  
      self.NumberOfDays:int = obj["NumberOfDays"]
      """  Used for Terms Type (X Months + Y Days)  """  
      self.MinimumDays:int = obj["MinimumDays"]
      """  Used for Terms Type (Days of Month)  """  
      self.DueOnDay:int = obj["DueOnDay"]
      """  Used for Terms Type (Day of Months)  """  
      self.NumberOfMonths:int = obj["NumberOfMonths"]
      """  Used for Terms Type (X Months + Y Days)  """  
      self.DiscountType:str = obj["DiscountType"]
      """  This field defines the type of the Discount  """  
      self.PartPayment:bool = obj["PartPayment"]
      """  Field to define when apply the discount percentage, can be when invoice is paid in full or Cash amount  """  
      self.ReqLOC:bool = obj["ReqLOC"]
      """  Require Letter of Credit.  """  
      self.GlobalTerms:bool = obj["GlobalTerms"]
      """  Marks this Terms as global, available to be sent out to other companies.  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Disables this record from receiving global updates.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.COIFRSCalculation:bool = obj["COIFRSCalculation"]
      """  COIFRSCalculation  """  
      self.COIFRSNumberOfPeriods:int = obj["COIFRSNumberOfPeriods"]
      """  COIFRSNumberOfPeriods  """  
      self.SystemDefault:bool = obj["SystemDefault"]
      """  Indicates if this terms is the system default  """  
      self.MonthlyDueDay:int = obj["MonthlyDueDay"]
      self.MonthlyOffset:int = obj["MonthlyOffset"]
      self.NonMonthlyDueDay:int = obj["NonMonthlyDueDay"]
      self.IsDefault:bool = obj["IsDefault"]
      """  Indicate if the term is default  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_TermsSchedRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.TermsCode:str = obj["TermsCode"]
      """  Unique identifier of the terms assigned by the user.  """  
      self.PaySeq:int = obj["PaySeq"]
      """  Specifies the number of payment of the Payment Schedule. This is an auto-generated sequence number.  """  
      self.PayDays:int = obj["PayDays"]
      """  Specifies the number of days for the payment to be paid. This is used to calculate Due Date in Invoice Payment Schedule.  """  
      self.PayPercent:int = obj["PayPercent"]
      """  Specifies the percent of the payment to be paid. This is used to calculate amount to be paid per payment in Sales Order and Invoice Payment Sechedule.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_TermsTableset:
   def __init__(self, obj):
      self.Terms:list[Erp_Tablesets_TermsRow] = obj["Terms"]
      self.TermsAttch:list[Erp_Tablesets_TermsAttchRow] = obj["TermsAttch"]
      self.LangDesc:list[Erp_Tablesets_LangDescRow] = obj["LangDesc"]
      self.TermsDtl:list[Erp_Tablesets_TermsDtlRow] = obj["TermsDtl"]
      self.TermsSched:list[Erp_Tablesets_TermsSchedRow] = obj["TermsSched"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_UpdExtTermsTableset:
   def __init__(self, obj):
      self.Terms:list[Erp_Tablesets_TermsRow] = obj["Terms"]
      self.TermsAttch:list[Erp_Tablesets_TermsAttchRow] = obj["TermsAttch"]
      self.LangDesc:list[Erp_Tablesets_LangDescRow] = obj["LangDesc"]
      self.TermsDtl:list[Erp_Tablesets_TermsDtlRow] = obj["TermsDtl"]
      self.TermsSched:list[Erp_Tablesets_TermsSchedRow] = obj["TermsSched"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetByID_input:
   """ Required : 
   termsCode
   """  
   def __init__(self, obj):
      self.termsCode:str = obj["termsCode"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_TermsTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_TermsTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_TermsTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_TermsListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
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
      self.ds:list[Erp_Tablesets_TermsTableset] = obj["ds"]
      self.tableName:str = obj["tableName"]
      self.key1:str = obj["key1"]
      self.key2:str = obj["key2"]
      self.key3:str = obj["key3"]
      pass

class GetNewLangDesc_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_TermsTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewTermsAttch_input:
   """ Required : 
   ds
   termsCode
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_TermsTableset] = obj["ds"]
      self.termsCode:str = obj["termsCode"]
      pass

class GetNewTermsAttch_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_TermsTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewTermsDtl_input:
   """ Required : 
   ds
   termsCode
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_TermsTableset] = obj["ds"]
      self.termsCode:str = obj["termsCode"]
      pass

class GetNewTermsDtl_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_TermsTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewTermsSched_input:
   """ Required : 
   ds
   termsCode
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_TermsTableset] = obj["ds"]
      self.termsCode:str = obj["termsCode"]
      pass

class GetNewTermsSched_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_TermsTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewTerms_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_TermsTableset] = obj["ds"]
      pass

class GetNewTerms_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_TermsTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseTerms
   whereClauseTermsAttch
   whereClauseLangDesc
   whereClauseTermsDtl
   whereClauseTermsSched
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseTerms:str = obj["whereClauseTerms"]
      self.whereClauseTermsAttch:str = obj["whereClauseTermsAttch"]
      self.whereClauseLangDesc:str = obj["whereClauseLangDesc"]
      self.whereClauseTermsDtl:str = obj["whereClauseTermsDtl"]
      self.whereClauseTermsSched:str = obj["whereClauseTermsSched"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_TermsTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetTermsSched_input:
   """ Required : 
   termsCode
   termsSchedTable
   """  
   def __init__(self, obj):
      self.termsCode:str = obj["termsCode"]
      self.termsSchedTable:object
      pass

class GetTermsSched_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.termsSchedTable:list = obj[any]
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

class OnChangingDisDays_input:
   """ Required : 
   vDueOnDay
   ds
   """  
   def __init__(self, obj):
      self.vDueOnDay:int = obj["vDueOnDay"]
      """  Propose Discount Days  """  
      self.ds:list[Erp_Tablesets_TermsTableset] = obj["ds"]
      pass

class OnChangingDisDays_output:
   def __init__(self, obj):
      pass

class OnChangingDisPercent_input:
   """ Required : 
   vDiscountPercent
   ds
   """  
   def __init__(self, obj):
      self.vDiscountPercent:int = obj["vDiscountPercent"]
      """  Propose Discount Days  """  
      self.ds:list[Erp_Tablesets_TermsTableset] = obj["ds"]
      pass

class OnChangingDisPercent_output:
   def __init__(self, obj):
      pass

class OnChangingNumOfDays_input:
   """ Required : 
   vNumOfDay
   ds
   """  
   def __init__(self, obj):
      self.vNumOfDay:int = obj["vNumOfDay"]
      """  Propose Discount Days  """  
      self.ds:list[Erp_Tablesets_TermsTableset] = obj["ds"]
      pass

class OnChangingNumOfDays_output:
   def __init__(self, obj):
      pass

class OnChangingNumOfMonths_input:
   """ Required : 
   vNumOfMonths
   ds
   """  
   def __init__(self, obj):
      self.vNumOfMonths:int = obj["vNumOfMonths"]
      """  Propose Discount Days  """  
      self.ds:list[Erp_Tablesets_TermsTableset] = obj["ds"]
      pass

class OnChangingNumOfMonths_output:
   def __init__(self, obj):
      pass

class OnChangingTermDueOnDay_input:
   """ Required : 
   pDueOnDay
   """  
   def __init__(self, obj):
      self.pDueOnDay:int = obj["pDueOnDay"]
      """  Propose Discount Days  """  
      pass

class OnChangingTermDueOnDay_output:
   def __init__(self, obj):
      pass

class OnTermsSchedPercentageUpdate_input:
   """ Required : 
   ts
   """  
   def __init__(self, obj):
      self.ts:list[Erp_Tablesets_TermsTableset] = obj["ts"]
      pass

class OnTermsSchedPercentageUpdate_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ts:list[Erp_Tablesets_TermsTableset] = obj["ts"]
      pass

      """  output parameters  """  

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtTermsTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtTermsTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_TermsTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_TermsTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ValidateDiscountPercent_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_TermsTableset] = obj["ds"]
      pass

class ValidateDiscountPercent_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_TermsTableset] = obj["ds"]
      self.warningMessage:str = obj["parameters"]
      pass

      """  output parameters  """  

