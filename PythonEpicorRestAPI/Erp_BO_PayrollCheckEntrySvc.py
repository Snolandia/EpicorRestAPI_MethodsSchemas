import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.PayrollCheckEntrySvc
# Description: 
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PayrollCheckEntrySvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PayrollCheckEntrySvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_PayrollCheckEntries(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get PayrollCheckEntries items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PayrollCheckEntries
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PRCheckRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PayrollCheckEntrySvc/PayrollCheckEntries",headers=creds) as resp:
           return await resp.json()

async def post_PayrollCheckEntries(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PayrollCheckEntries
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PRCheckRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PRCheckRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PayrollCheckEntrySvc/PayrollCheckEntries", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_PayrollCheckEntries_Company_HeadNum(Company, HeadNum, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PayrollCheckEntry item
   Description: Calls GetByID to retrieve the PayrollCheckEntry item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PayrollCheckEntry
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param HeadNum: Desc: HeadNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PRCheckRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PayrollCheckEntrySvc/PayrollCheckEntries(" + Company + "," + HeadNum + ")",headers=creds) as resp:
           return await resp.json()

async def patch_PayrollCheckEntries_Company_HeadNum(Company, HeadNum, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update PayrollCheckEntry for the service
   Description: Calls UpdateExt to update PayrollCheckEntry. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PayrollCheckEntry
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param HeadNum: Desc: HeadNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PRCheckRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.PayrollCheckEntrySvc/PayrollCheckEntries(" + Company + "," + HeadNum + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_PayrollCheckEntries_Company_HeadNum(Company, HeadNum, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete PayrollCheckEntry item
   Description: Call UpdateExt to delete PayrollCheckEntry item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PayrollCheckEntry
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param HeadNum: Desc: HeadNum   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.PayrollCheckEntrySvc/PayrollCheckEntries(" + Company + "," + HeadNum + ")",headers=creds) as resp:
           return await resp.json()

async def get_PayrollCheckEntries_Company_HeadNum_PRCheckTGLCs(Company, HeadNum, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get PRCheckTGLCs items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_PRCheckTGLCs1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param HeadNum: Desc: HeadNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PRCheckTGLCRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PayrollCheckEntrySvc/PayrollCheckEntries(" + Company + "," + HeadNum + ")/PRCheckTGLCs",headers=creds) as resp:
           return await resp.json()

async def get_PayrollCheckEntries_Company_HeadNum_PRCheckTGLCs_Company_HeadNum_TGLCTranNum_Key2(Company, HeadNum, TGLCTranNum, Key2, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PRCheckTGLC item
   Description: Calls GetByID to retrieve the PRCheckTGLC item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PRCheckTGLC1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param HeadNum: Desc: HeadNum   Required: True
      :param TGLCTranNum: Desc: TGLCTranNum   Required: True
      :param Key2: Desc: Key2   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PRCheckTGLCRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PayrollCheckEntrySvc/PayrollCheckEntries(" + Company + "," + HeadNum + ")/PRCheckTGLCs(" + Company + "," + HeadNum + "," + TGLCTranNum + "," + Key2 + ")",headers=creds) as resp:
           return await resp.json()

async def get_PayrollCheckEntries_Company_HeadNum_PRChkDeds(Company, HeadNum, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get PRChkDeds items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_PRChkDeds1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param HeadNum: Desc: HeadNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PRChkDedRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PayrollCheckEntrySvc/PayrollCheckEntries(" + Company + "," + HeadNum + ")/PRChkDeds",headers=creds) as resp:
           return await resp.json()

async def get_PayrollCheckEntries_Company_HeadNum_PRChkDeds_Company_HeadNum_DeductionID_DeductionNum(Company, HeadNum, DeductionID, DeductionNum, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PRChkDed item
   Description: Calls GetByID to retrieve the PRChkDed item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PRChkDed1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param HeadNum: Desc: HeadNum   Required: True
      :param DeductionID: Desc: DeductionID   Required: True   Allow empty value : True
      :param DeductionNum: Desc: DeductionNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PRChkDedRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PayrollCheckEntrySvc/PayrollCheckEntries(" + Company + "," + HeadNum + ")/PRChkDeds(" + Company + "," + HeadNum + "," + DeductionID + "," + DeductionNum + ")",headers=creds) as resp:
           return await resp.json()

async def get_PayrollCheckEntries_Company_HeadNum_PRChkDtls(Company, HeadNum, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get PRChkDtls items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_PRChkDtls1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param HeadNum: Desc: HeadNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PRChkDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PayrollCheckEntrySvc/PayrollCheckEntries(" + Company + "," + HeadNum + ")/PRChkDtls",headers=creds) as resp:
           return await resp.json()

async def get_PayrollCheckEntries_Company_HeadNum_PRChkDtls_Company_HeadNum_LineNum(Company, HeadNum, LineNum, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PRChkDtl item
   Description: Calls GetByID to retrieve the PRChkDtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PRChkDtl1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param HeadNum: Desc: HeadNum   Required: True
      :param LineNum: Desc: LineNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PRChkDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PayrollCheckEntrySvc/PayrollCheckEntries(" + Company + "," + HeadNum + ")/PRChkDtls(" + Company + "," + HeadNum + "," + LineNum + ")",headers=creds) as resp:
           return await resp.json()

async def get_PayrollCheckEntries_Company_HeadNum_PRChkTaxes(Company, HeadNum, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get PRChkTaxes items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_PRChkTaxes1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param HeadNum: Desc: HeadNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PRChkTaxRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PayrollCheckEntrySvc/PayrollCheckEntries(" + Company + "," + HeadNum + ")/PRChkTaxes",headers=creds) as resp:
           return await resp.json()

async def get_PayrollCheckEntries_Company_HeadNum_PRChkTaxes_Company_HeadNum_TaxTblID(Company, HeadNum, TaxTblID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PRChkTax item
   Description: Calls GetByID to retrieve the PRChkTax item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PRChkTax1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param HeadNum: Desc: HeadNum   Required: True
      :param TaxTblID: Desc: TaxTblID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PRChkTaxRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PayrollCheckEntrySvc/PayrollCheckEntries(" + Company + "," + HeadNum + ")/PRChkTaxes(" + Company + "," + HeadNum + "," + TaxTblID + ")",headers=creds) as resp:
           return await resp.json()

async def get_PRCheckTGLCs(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get PRCheckTGLCs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PRCheckTGLCs
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PRCheckTGLCRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PayrollCheckEntrySvc/PRCheckTGLCs",headers=creds) as resp:
           return await resp.json()

async def post_PRCheckTGLCs(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PRCheckTGLCs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PRCheckTGLCRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PRCheckTGLCRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PayrollCheckEntrySvc/PRCheckTGLCs", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_PRCheckTGLCs_Company_HeadNum_TGLCTranNum_Key2(Company, HeadNum, TGLCTranNum, Key2, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PRCheckTGLC item
   Description: Calls GetByID to retrieve the PRCheckTGLC item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PRCheckTGLC
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param HeadNum: Desc: HeadNum   Required: True
      :param TGLCTranNum: Desc: TGLCTranNum   Required: True
      :param Key2: Desc: Key2   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PRCheckTGLCRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PayrollCheckEntrySvc/PRCheckTGLCs(" + Company + "," + HeadNum + "," + TGLCTranNum + "," + Key2 + ")",headers=creds) as resp:
           return await resp.json()

async def patch_PRCheckTGLCs_Company_HeadNum_TGLCTranNum_Key2(Company, HeadNum, TGLCTranNum, Key2, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update PRCheckTGLC for the service
   Description: Calls UpdateExt to update PRCheckTGLC. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PRCheckTGLC
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param HeadNum: Desc: HeadNum   Required: True
      :param TGLCTranNum: Desc: TGLCTranNum   Required: True
      :param Key2: Desc: Key2   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PRCheckTGLCRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.PayrollCheckEntrySvc/PRCheckTGLCs(" + Company + "," + HeadNum + "," + TGLCTranNum + "," + Key2 + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_PRCheckTGLCs_Company_HeadNum_TGLCTranNum_Key2(Company, HeadNum, TGLCTranNum, Key2, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete PRCheckTGLC item
   Description: Call UpdateExt to delete PRCheckTGLC item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PRCheckTGLC
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param HeadNum: Desc: HeadNum   Required: True
      :param TGLCTranNum: Desc: TGLCTranNum   Required: True
      :param Key2: Desc: Key2   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.PayrollCheckEntrySvc/PRCheckTGLCs(" + Company + "," + HeadNum + "," + TGLCTranNum + "," + Key2 + ")",headers=creds) as resp:
           return await resp.json()

async def get_PRChkDeds(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get PRChkDeds items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PRChkDeds
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PRChkDedRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PayrollCheckEntrySvc/PRChkDeds",headers=creds) as resp:
           return await resp.json()

async def post_PRChkDeds(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PRChkDeds
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PRChkDedRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PRChkDedRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PayrollCheckEntrySvc/PRChkDeds", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_PRChkDeds_Company_HeadNum_DeductionID_DeductionNum(Company, HeadNum, DeductionID, DeductionNum, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PRChkDed item
   Description: Calls GetByID to retrieve the PRChkDed item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PRChkDed
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param HeadNum: Desc: HeadNum   Required: True
      :param DeductionID: Desc: DeductionID   Required: True   Allow empty value : True
      :param DeductionNum: Desc: DeductionNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PRChkDedRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PayrollCheckEntrySvc/PRChkDeds(" + Company + "," + HeadNum + "," + DeductionID + "," + DeductionNum + ")",headers=creds) as resp:
           return await resp.json()

async def patch_PRChkDeds_Company_HeadNum_DeductionID_DeductionNum(Company, HeadNum, DeductionID, DeductionNum, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update PRChkDed for the service
   Description: Calls UpdateExt to update PRChkDed. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PRChkDed
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param HeadNum: Desc: HeadNum   Required: True
      :param DeductionID: Desc: DeductionID   Required: True   Allow empty value : True
      :param DeductionNum: Desc: DeductionNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PRChkDedRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.PayrollCheckEntrySvc/PRChkDeds(" + Company + "," + HeadNum + "," + DeductionID + "," + DeductionNum + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_PRChkDeds_Company_HeadNum_DeductionID_DeductionNum(Company, HeadNum, DeductionID, DeductionNum, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete PRChkDed item
   Description: Call UpdateExt to delete PRChkDed item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PRChkDed
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param HeadNum: Desc: HeadNum   Required: True
      :param DeductionID: Desc: DeductionID   Required: True   Allow empty value : True
      :param DeductionNum: Desc: DeductionNum   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.PayrollCheckEntrySvc/PRChkDeds(" + Company + "," + HeadNum + "," + DeductionID + "," + DeductionNum + ")",headers=creds) as resp:
           return await resp.json()

async def get_PRChkDtls(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get PRChkDtls items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PRChkDtls
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PRChkDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PayrollCheckEntrySvc/PRChkDtls",headers=creds) as resp:
           return await resp.json()

async def post_PRChkDtls(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PRChkDtls
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PRChkDtlRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PRChkDtlRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PayrollCheckEntrySvc/PRChkDtls", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_PRChkDtls_Company_HeadNum_LineNum(Company, HeadNum, LineNum, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PRChkDtl item
   Description: Calls GetByID to retrieve the PRChkDtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PRChkDtl
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param HeadNum: Desc: HeadNum   Required: True
      :param LineNum: Desc: LineNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PRChkDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PayrollCheckEntrySvc/PRChkDtls(" + Company + "," + HeadNum + "," + LineNum + ")",headers=creds) as resp:
           return await resp.json()

async def patch_PRChkDtls_Company_HeadNum_LineNum(Company, HeadNum, LineNum, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update PRChkDtl for the service
   Description: Calls UpdateExt to update PRChkDtl. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PRChkDtl
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param HeadNum: Desc: HeadNum   Required: True
      :param LineNum: Desc: LineNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PRChkDtlRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.PayrollCheckEntrySvc/PRChkDtls(" + Company + "," + HeadNum + "," + LineNum + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_PRChkDtls_Company_HeadNum_LineNum(Company, HeadNum, LineNum, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete PRChkDtl item
   Description: Call UpdateExt to delete PRChkDtl item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PRChkDtl
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param HeadNum: Desc: HeadNum   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.PayrollCheckEntrySvc/PRChkDtls(" + Company + "," + HeadNum + "," + LineNum + ")",headers=creds) as resp:
           return await resp.json()

async def get_PRChkTaxes(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get PRChkTaxes items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PRChkTaxes
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PRChkTaxRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PayrollCheckEntrySvc/PRChkTaxes",headers=creds) as resp:
           return await resp.json()

async def post_PRChkTaxes(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PRChkTaxes
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PRChkTaxRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PRChkTaxRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PayrollCheckEntrySvc/PRChkTaxes", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_PRChkTaxes_Company_HeadNum_TaxTblID(Company, HeadNum, TaxTblID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PRChkTax item
   Description: Calls GetByID to retrieve the PRChkTax item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PRChkTax
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param HeadNum: Desc: HeadNum   Required: True
      :param TaxTblID: Desc: TaxTblID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PRChkTaxRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PayrollCheckEntrySvc/PRChkTaxes(" + Company + "," + HeadNum + "," + TaxTblID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_PRChkTaxes_Company_HeadNum_TaxTblID(Company, HeadNum, TaxTblID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update PRChkTax for the service
   Description: Calls UpdateExt to update PRChkTax. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PRChkTax
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param HeadNum: Desc: HeadNum   Required: True
      :param TaxTblID: Desc: TaxTblID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PRChkTaxRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.PayrollCheckEntrySvc/PRChkTaxes(" + Company + "," + HeadNum + "," + TaxTblID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_PRChkTaxes_Company_HeadNum_TaxTblID(Company, HeadNum, TaxTblID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete PRChkTax item
   Description: Call UpdateExt to delete PRChkTax item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PRChkTax
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param HeadNum: Desc: HeadNum   Required: True
      :param TaxTblID: Desc: TaxTblID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.PayrollCheckEntrySvc/PRChkTaxes(" + Company + "," + HeadNum + "," + TaxTblID + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PRCheckListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PayrollCheckEntrySvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClausePRCheck, whereClausePRChkDed, whereClausePRChkDtl, whereClausePRChkTax, whereClausePRCheckTGLC, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClausePRCheck=" + whereClausePRCheck
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClausePRChkDed=" + whereClausePRChkDed
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClausePRChkDtl=" + whereClausePRChkDtl
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClausePRChkTax=" + whereClausePRChkTax
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClausePRCheckTGLC=" + whereClausePRCheckTGLC
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PayrollCheckEntrySvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(headNum, epicorHeaders = None):
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
   params += "headNum=" + headNum

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PayrollCheckEntrySvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PayrollCheckEntrySvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PayrollCheckEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_getClientFileName(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method getClientFileName
   OperationID: getClientFileName
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/getClientFileName_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/getClientFileName_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PayrollCheckEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CalculateDeductsAndTaxes(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CalculateDeductsAndTaxes
   Description: Method to call to calculate deductions and taxes.
   OperationID: CalculateDeductsAndTaxes
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CalculateDeductsAndTaxes_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CalculateDeductsAndTaxes_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PayrollCheckEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CalculateOvertime(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CalculateOvertime
   Description: Method to call to calculate overtime.
   OperationID: CalculateOvertime
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CalculateOvertime_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CalculateOvertime_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PayrollCheckEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CalculateOvertimeVerification(epicorHeaders = None):
   """  
   Summary: Invoke method CalculateOvertimeVerification
   Description: Method to call prior to calling CalculateOvertime.  This method will
return text of a verification message to ask the user to verify the
process should run.  The question is yes-no.  If the answer is yes, proceed
with the calculation of overtime.  If the answer is no, cancel the
calculation of overtime.
   OperationID: CalculateOvertimeVerification
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/CalculateOvertimeVerification_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PayrollCheckEntrySvc/List",headers=creds) as resp:
           return await resp.json()

async def post_ChangePRCheckEmpID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangePRCheckEmpID
   Description: Method to call to when the Employee ID changes.  This method will set
employee fields in PRCheck based on the new employee id.
   OperationID: ChangePRCheckEmpID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangePRCheckEmpID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangePRCheckEmpID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PayrollCheckEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangePRChkDtlAmountType(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangePRChkDtlAmountType
   Description: Method to call to when the Check Detail Amount Type changes.  This method
will reset values for the new amount type.
   OperationID: ChangePRChkDtlAmountType
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangePRChkDtlAmountType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangePRChkDtlAmountType_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PayrollCheckEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangePRChkDtlBaseHours(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangePRChkDtlBaseHours
   Description: Method to call to when the Check Detail Base Hours changes.  This method
will recalculate detail values based on the new hours.
   OperationID: ChangePRChkDtlBaseHours
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangePRChkDtlBaseHours_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangePRChkDtlBaseHours_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PayrollCheckEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_RecalcPayRate(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method RecalcPayRate
   Description: Method to recalculate the pay rate for salaried employees so the base pay will be the same regardless.
   OperationID: RecalcPayRate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/RecalcPayRate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RecalcPayRate_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PayrollCheckEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangePRChkDtlBasePay(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangePRChkDtlBasePay
   Description: Method to call to when the Check Detail Base Pay changes.  This method
will recalculate detail values based on the new base pay amount.
   OperationID: ChangePRChkDtlBasePay
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangePRChkDtlBasePay_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangePRChkDtlBasePay_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PayrollCheckEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangePRChkDtlPayRate(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangePRChkDtlPayRate
   Description: Method to call to when the Check Detail Pay Rate changes.  This method
will recalculate detail values based on the new pay rate.
   OperationID: ChangePRChkDtlPayRate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangePRChkDtlPayRate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangePRChkDtlPayRate_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PayrollCheckEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangePRChkDtlPayrollDate(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangePRChkDtlPayrollDate
   Description: Method to call to when the Check Detail Payroll Date changes.  This method
will recalculate detail values if the amount type is calculated.
   OperationID: ChangePRChkDtlPayrollDate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangePRChkDtlPayrollDate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangePRChkDtlPayrollDate_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PayrollCheckEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangePRChkDtlPayTypeID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangePRChkDtlPayTypeID
   Description: Method to call to when the Check Detail Pay Type changes.  This method
will recalculate detail values based on the new pay type.
   OperationID: ChangePRChkDtlPayTypeID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangePRChkDtlPayTypeID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangePRChkDtlPayTypeID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PayrollCheckEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangePRChkDtlPremiumHours(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangePRChkDtlPremiumHours
   Description: Method to call to when the Check Detail Premium Hours changes.  This method
will recalculate detail values based on the new hours.
   OperationID: ChangePRChkDtlPremiumHours
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangePRChkDtlPremiumHours_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangePRChkDtlPremiumHours_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PayrollCheckEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangePRChkDtlPremiumPayType(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangePRChkDtlPremiumPayType
   Description: Method to call to when the Check Detail Premium Pay Type changes.  This method
will recalculate detail values based on the new pay type.
   OperationID: ChangePRChkDtlPremiumPayType
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangePRChkDtlPremiumPayType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangePRChkDtlPremiumPayType_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PayrollCheckEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangePRChkDtlShift(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangePRChkDtlShift
   Description: Method to call to when the Check Detail Shift changes.  This method
will reassign values based on the new shift.
   OperationID: ChangePRChkDtlShift
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangePRChkDtlShift_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangePRChkDtlShift_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PayrollCheckEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckDocumentIsLocked(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckDocumentIsLocked
   Description: Method to call when it is necessary to check if document is lock, before doing smth.
   OperationID: CheckDocumentIsLocked
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckDocumentIsLocked_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckDocumentIsLocked_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PayrollCheckEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckPrinted(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckPrinted
   Description: Method to call to retrieve the text of the question to ask the user when
checks have been printed.  This question is asked when the user attempts to
add hours, update hours, delete hours, update deductions, or update taxes to
a check.
   OperationID: CheckPrinted
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckPrinted_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckPrinted_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PayrollCheckEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ElecFileDownloaded(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ElecFileDownloaded
   Description: Method to call to retrieve the text of the question to ask the user when
electronic deposit files have been generated.  This question is asked when the user attempts to
add hours, update hours, delete hours, update deductions, or update taxes to
a check.
   OperationID: ElecFileDownloaded
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ElecFileDownloaded_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ElecFileDownloaded_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PayrollCheckEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GeneratePayChecks(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GeneratePayChecks
   Description: Method to call to generate paychecks.
   OperationID: GeneratePayChecks
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GeneratePayChecks_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GeneratePayChecks_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PayrollCheckEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GeneratePayChecksVerification(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GeneratePayChecksVerification
   Description: Method to call prior to calling GeneratePaychecks.  This method will
return text of a verification message to ask the user to verify the
process should run.  The question is yes-no.  If the answer is yes, proceed
with the check generation.  If the answer is no, cancel the check generation.
   OperationID: GeneratePayChecksVerification
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GeneratePayChecksVerification_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GeneratePayChecksVerification_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PayrollCheckEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetGLEntries(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetGLEntries
   Description: Retrieves the GL transactions for each check.
   OperationID: GetGLEntries
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetGLEntries_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetGLEntries_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PayrollCheckEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewPRCheckForGroup(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewPRCheckForGroup
   Description: Method to call to get a new PRCheck record..
   OperationID: GetNewPRCheckForGroup
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPRCheckForGroup_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPRCheckForGroup_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PayrollCheckEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetRowsByEmpID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetRowsByEmpID
   Description: Validates the FromOpCode field and poplutes the From OpCode description.  Is called when
the From Op Code changes.  If the code is not valid, an exception will be thrown.
   OperationID: GetRowsByEmpID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetRowsByEmpID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRowsByEmpID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PayrollCheckEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetRowsFromAutoBankRec(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetRowsFromAutoBankRec
   Description: Called from Automated Bank Reconciliation
   OperationID: GetRowsFromAutoBankRec
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetRowsFromAutoBankRec_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRowsFromAutoBankRec_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PayrollCheckEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_UpdatePRChkDed(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method UpdatePRChkDed
   Description: Method to call to update a PRChkDed record.  This method should be called
in place of the standard Update method when updating a PRChkDed record.
   OperationID: UpdatePRChkDed
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdatePRChkDed_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdatePRChkDed_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PayrollCheckEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_UpdatePRChkTax(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method UpdatePRChkTax
   Description: Method to call to update a PRChkTax record.  This method should be called
in place of the standard Update method when updating a PRChkTax record.
   OperationID: UpdatePRChkTax
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdatePRChkTax_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdatePRChkTax_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PayrollCheckEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewPRCheck(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewPRCheck
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPRCheck
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPRCheck_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPRCheck_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PayrollCheckEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewPRChkDed(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewPRChkDed
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPRChkDed
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPRChkDed_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPRChkDed_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PayrollCheckEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewPRChkDtl(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewPRChkDtl
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPRChkDtl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPRChkDtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPRChkDtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PayrollCheckEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewPRChkTax(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewPRChkTax
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPRChkTax
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPRChkTax_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPRChkTax_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PayrollCheckEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewPRCheckTGLC(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewPRCheckTGLC
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPRCheckTGLC
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPRCheckTGLC_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPRCheckTGLC_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PayrollCheckEntrySvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PayrollCheckEntrySvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PayrollCheckEntrySvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PayrollCheckEntrySvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PayrollCheckEntrySvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PayrollCheckEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PRCheckListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PRCheckListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PRCheckRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PRCheckRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PRCheckTGLCRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PRCheckTGLCRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PRChkDedRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PRChkDedRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PRChkDtlRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PRChkDtlRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PRChkTaxRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PRChkTaxRow] = obj["value"]
      pass

class Erp_Tablesets_PRCheckListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.Posted:bool = obj["Posted"]
      """  An internal flag which indicates if this check has been Posted.  If "NO" then it is  considered as still being in the data entry mode. In which case it is still accessible by the check entry programs.  It is set to "Yes" by the posting process.  """  
      self.GroupID:str = obj["GroupID"]
      """  The data entry "Group" that the check belongs to.  All checks belong to a "Group."  It is assigned to the record during creation using the "current group" that the user is signed into.  It cannot be changed.  The GroupID is used to selectively print and post.  """  
      self.HeadNum:int = obj["HeadNum"]
      """  An integer automatically assigned by the system using the database sequence called "PRCheckSeq".  HeadNum + Company creates a unique key for the record. This is for internal control only the user never needs to reference.  """  
      self.EmpLink:str = obj["EmpLink"]
      """  Encoded value which identifies the employee.  """  
      self.BankAcctID:str = obj["BankAcctID"]
      """  BankAcctId of the BankAcct master that this check was drawn  against. This field is updated during the check printing process for system printed checks or entered by the user for manually printed checks. It must be entered and valid for manual checks. It is invalid if not found or BankAcct.Active = No.  """  
      self.CheckNum:int = obj["CheckNum"]
      """  Check number is assigned during the check printing process for checks that are printed by the system or entered by the user for hand written checks. NOTE:  Posting of the group is not allowed if any CheckHed record exits with a zero check.  """  
      self.CheckDate:str = obj["CheckDate"]
      """  Check Date is assigned during the printing process for system printed checks or entered by the user for hand written checks.  """  
      self.PSDate:str = obj["PSDate"]
      """  Pay period start date for this check.  This is updated as part of the payroll posting process for system generated checks.  It is entered by the user for manual checks.  """  
      self.PEDate:str = obj["PEDate"]
      """  Pay period end date for this check.  This is updated as part of the payroll posting process for system generated checks.  It is entered by the user for manual checks.  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """  Fiscal Year that the check is posted to.  Updated during the check printing process for system printed checks or updated based on the CheckDate for hand written checks.  """  
      self.FiscalPeriod:int = obj["FiscalPeriod"]
      """  G/L fiscal period that this check is posted to.  Updated by the check printing process for system printed checks.  For hand written checks it updated by check entry program based on the check date.  """  
      self.Voided:bool = obj["Voided"]
      """  Voided flag  """  
      self.TotalBasePay:int = obj["TotalBasePay"]
      """  Total Base Pay for this check. Not user maintainable.  It summarizes all PRChkDtl for the check.  Updated via PRChkDtl write/delete triggers. The triggers update this with  (BasePay + PremiumPay + PremiumBasePay + ShiftPay)  """  
      self.TotalPremiumPay:int = obj["TotalPremiumPay"]
      """  Total Premium Pay for this check.  Not user maintainable.  It summarizes all PRChkDtl.PremiumPay for the check.  Updated via PRChkDtl write/delete triggers.  """  
      self.TotalShiftPay:int = obj["TotalShiftPay"]
      """  Total Shift Pay for this check.  Not user maintainable.  It summarizes all PRChkDtl.ShiftPay for the check.  Updated via PRChkDtl write/delete triggers.  """  
      self.TotalTaxes:int = obj["TotalTaxes"]
      """  Total of all Tax amounts for the check.  Not user maintainable.  It summarizes all PRChkTax.TaxAmt for the check.  Updated via PRChkTax write/delete triggers.  """  
      self.TotalDeductions:int = obj["TotalDeductions"]
      """  Total of all deduction amounts for the check.  Not user maintainable.  It summarizes all PRChkDed.DeductionAmt for the check.  Updated via PRChkDed write/delete triggers.  """  
      self.TotalBaseHours:int = obj["TotalBaseHours"]
      """  Total Base Hours on this check. Not directly maintainable by user. A summary of PRChkDtl.BaseHours updated via the PRChkDtl write/delete triggers  """  
      self.TotalPremiumHours:int = obj["TotalPremiumHours"]
      """  Total Premium Hours on this check. Not directly maintainable by user. A summary of PRChkDtl.PremiumHours updated via the PRChkDtl write/delete triggers  """  
      self.CheckAmt:int = obj["CheckAmt"]
      """  Net Check Amount.  Not directly user maintainable.  Updated as (PRCheck.TotalBasePay + TotalPremiumPay + ShiftPay + NonTaxAmt) - (TotalTaxes + TotalDeductions).  Updated via write trigger on PRCheck.  """  
      self.StartupCheck:bool = obj["StartupCheck"]
      """  Indicates that the check was created using the YTD Startup routines.  This is not a real check.  """  
      self.EntryPerson:str = obj["EntryPerson"]
      """  UserID that created the Check. Assign by the system using the current UserID at the time the record was created.  """  
      self.WorkCompCode:str = obj["WorkCompCode"]
      """  The WorkCompCode relates this check to the proper WorkComp master.  Used in the Worker's Comp report.  It is duplicated from the PREmpMas.WorkCompCode during the posting process.  """  
      self.ClassID:str = obj["ClassID"]
      """  Payroll class ID that employee is currently assigned to. A mirror image of PREmpMas. It is kept in sync by the PREmpMas write trigger.  """  
      self.Note:str = obj["Note"]
      """  A short note which is printed on the check.  """  
      self.PayFrequency:str = obj["PayFrequency"]
      """  Copied from PREmpMas at the time the PRCheck record is created.  """  
      self.ClearedCheck:bool = obj["ClearedCheck"]
      """  Indicates the check's cleared status.  When the Bank Statement is posted all Pending Transactions and Checks are flagged as Cleared and any variances are posted to the Bank Account's Cash and Cleared Variance Accounts.  """  
      self.ClearedPending:bool = obj["ClearedPending"]
      """  Indicates that the check is in the process of being cleared.  When the Bank Statement is posted all Pending Transactions and Checks are flagged as Cleared and any variances are posted to the Bank Account's Cash and Cleared Variance Accounts.  """  
      self.ClearedAmt:int = obj["ClearedAmt"]
      """  Amount that the bank cleared the check for.  """  
      self.ClearedPerson:str = obj["ClearedPerson"]
      """  Person who cleared the check (System Set).  """  
      self.ClearedDate:str = obj["ClearedDate"]
      """  Date that the check was cleared in the system (System Set).  """  
      self.ClearedTime:str = obj["ClearedTime"]
      """  Time that the check was cleared in the system - in HH:MM:SS format (System Set).  """  
      self.ClearedStmtEndDate:str = obj["ClearedStmtEndDate"]
      """  End Date of the Statement that the check was cleared on.  """  
      self.BankSlip:str = obj["BankSlip"]
      """  The identifier of the Bankslip document (bank statement) on which this transaction was cleared by the bank. This is updated via the bank reconciliation process.  This is also written to the related GLJrnDtl records.  """  
      self.CashBookNum:int = obj["CashBookNum"]
      """  This field identifies a bankslip.  """  
      self.CashbookLine:int = obj["CashbookLine"]
      """  This field identifies a line of a bankslip.  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  Fiscal year suffix.  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  The fiscal calendar year/suffix/period were derived from.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.MXRecDate:str = obj["MXRecDate"]
      """  MXRecDate  """  
      self.VoidedDate:str = obj["VoidedDate"]
      """  VoidedDate  """  
      self.SocSecNum:str = obj["SocSecNum"]
      self.EmpID:str = obj["EmpID"]
      self.AddressList:str = obj["AddressList"]
      self.EmpFirstName:str = obj["EmpFirstName"]
      self.EmpMiddleInit:str = obj["EmpMiddleInit"]
      self.EmpLastName:str = obj["EmpLastName"]
      self.PhotoFile:str = obj["PhotoFile"]
      self.ImageFile:str = obj["ImageFile"]
      self.PRInterfacedContinue:bool = obj["PRInterfacedContinue"]
      """  Used in VoidPRCheck - User response to a question when GL is not interfaced.  """  
      self.EmpLinkFirstName:str = obj["EmpLinkFirstName"]
      self.EmpLinkLastName:str = obj["EmpLinkLastName"]
      self.EmpLinkName:str = obj["EmpLinkName"]
      self.IsLcked:bool = obj["IsLcked"]
      """  shows is this invoice is blocked in RvLock.  """  
      self.RvnJrnUID:int = obj["RvnJrnUID"]
      """  Review Journal UID  """  
      self.LockStatus:str = obj["LockStatus"]
      """  locked means can not be posted: an invoice is already in review journal or in posting process.  """  
      self.BankAcctIDDescription:str = obj["BankAcctIDDescription"]
      """  Full description of the bank account.  """  
      self.BankAcctIDBankName:str = obj["BankAcctIDBankName"]
      """  The Bank's full name.  """  
      self.ClassIDDescription:str = obj["ClassIDDescription"]
      """  Full description of the payroll class.  """  
      self.WorkCompCodeDescription:str = obj["WorkCompCodeDescription"]
      """  Description of the workers' compensation code.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PRCheckRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.Posted:bool = obj["Posted"]
      """  An internal flag which indicates if this check has been Posted.  If "NO" then it is  considered as still being in the data entry mode. In which case it is still accessible by the check entry programs.  It is set to "Yes" by the posting process.  """  
      self.GroupID:str = obj["GroupID"]
      """  The data entry "Group" that the check belongs to.  All checks belong to a "Group."  It is assigned to the record during creation using the "current group" that the user is signed into.  It cannot be changed.  The GroupID is used to selectively print and post.  """  
      self.HeadNum:int = obj["HeadNum"]
      """  An integer automatically assigned by the system using the database sequence called "PRCheckSeq".  HeadNum + Company creates a unique key for the record. This is for internal control only the user never needs to reference.  """  
      self.EmpLink:str = obj["EmpLink"]
      """  Encoded value which identifies the employee.  """  
      self.BankAcctID:str = obj["BankAcctID"]
      """  BankAcctId of the BankAcct master that this check was drawn  against. This field is updated during the check printing process for system printed checks or entered by the user for manually printed checks. It must be entered and valid for manual checks. It is invalid if not found or BankAcct.Active = No.  """  
      self.CheckNum:int = obj["CheckNum"]
      """  Check number is assigned during the check printing process for checks that are printed by the system or entered by the user for hand written checks. NOTE:  Posting of the group is not allowed if any CheckHed record exits with a zero check.  """  
      self.CheckDate:str = obj["CheckDate"]
      """  Check Date is assigned during the printing process for system printed checks or entered by the user for hand written checks.  """  
      self.PSDate:str = obj["PSDate"]
      """  Pay period start date for this check.  This is updated as part of the payroll posting process for system generated checks.  It is entered by the user for manual checks.  """  
      self.PEDate:str = obj["PEDate"]
      """  Pay period end date for this check.  This is updated as part of the payroll posting process for system generated checks.  It is entered by the user for manual checks.  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """  Fiscal Year that the check is posted to.  Updated during the check printing process for system printed checks or updated based on the CheckDate for hand written checks.  """  
      self.FiscalPeriod:int = obj["FiscalPeriod"]
      """  G/L fiscal period that this check is posted to.  Updated by the check printing process for system printed checks.  For hand written checks it updated by check entry program based on the check date.  """  
      self.Voided:bool = obj["Voided"]
      """  Voided flag  """  
      self.TotalBasePay:int = obj["TotalBasePay"]
      """  Total Base Pay for this check. Not user maintainable.  It summarizes all PRChkDtl for the check.  Updated via PRChkDtl write/delete triggers. The triggers update this with  (BasePay + PremiumPay + PremiumBasePay + ShiftPay)  """  
      self.TotalPremiumPay:int = obj["TotalPremiumPay"]
      """  Total Premium Pay for this check.  Not user maintainable.  It summarizes all PRChkDtl.PremiumPay for the check.  Updated via PRChkDtl write/delete triggers.  """  
      self.TotalShiftPay:int = obj["TotalShiftPay"]
      """  Total Shift Pay for this check.  Not user maintainable.  It summarizes all PRChkDtl.ShiftPay for the check.  Updated via PRChkDtl write/delete triggers.  """  
      self.TotalTaxes:int = obj["TotalTaxes"]
      """  Total of all Tax amounts for the check.  Not user maintainable.  It summarizes all PRChkTax.TaxAmt for the check.  Updated via PRChkTax write/delete triggers.  """  
      self.TotalDeductions:int = obj["TotalDeductions"]
      """  Total of all deduction amounts for the check.  Not user maintainable.  It summarizes all PRChkDed.DeductionAmt for the check.  Updated via PRChkDed write/delete triggers.  """  
      self.TotalBaseHours:int = obj["TotalBaseHours"]
      """  Total Base Hours on this check. Not directly maintainable by user. A summary of PRChkDtl.BaseHours updated via the PRChkDtl write/delete triggers  """  
      self.TotalPremiumHours:int = obj["TotalPremiumHours"]
      """  Total Premium Hours on this check. Not directly maintainable by user. A summary of PRChkDtl.PremiumHours updated via the PRChkDtl write/delete triggers  """  
      self.CheckAmt:int = obj["CheckAmt"]
      """  Net Check Amount.  Not directly user maintainable.  Updated as (PRCheck.TotalBasePay + TotalPremiumPay + ShiftPay + NonTaxAmt) - (TotalTaxes + TotalDeductions).  Updated via write trigger on PRCheck.  """  
      self.StartupCheck:bool = obj["StartupCheck"]
      """  Indicates that the check was created using the YTD Startup routines.  This is not a real check.  """  
      self.EntryPerson:str = obj["EntryPerson"]
      """  UserID that created the Check. Assign by the system using the current UserID at the time the record was created.  """  
      self.WorkCompCode:str = obj["WorkCompCode"]
      """  The WorkCompCode relates this check to the proper WorkComp master.  Used in the Worker's Comp report.  It is duplicated from the PREmpMas.WorkCompCode during the posting process.  """  
      self.ClassID:str = obj["ClassID"]
      """  Payroll class ID that employee is currently assigned to. A mirror image of PREmpMas. It is kept in sync by the PREmpMas write trigger.  """  
      self.Note:str = obj["Note"]
      """  A short note which is printed on the check.  """  
      self.PayFrequency:str = obj["PayFrequency"]
      """  Copied from PREmpMas at the time the PRCheck record is created.  """  
      self.ClearedCheck:bool = obj["ClearedCheck"]
      """  Indicates the check's cleared status.  When the Bank Statement is posted all Pending Transactions and Checks are flagged as Cleared and any variances are posted to the Bank Account's Cash and Cleared Variance Accounts.  """  
      self.ClearedPending:bool = obj["ClearedPending"]
      """  Indicates that the check is in the process of being cleared.  When the Bank Statement is posted all Pending Transactions and Checks are flagged as Cleared and any variances are posted to the Bank Account's Cash and Cleared Variance Accounts.  """  
      self.ClearedAmt:int = obj["ClearedAmt"]
      """  Amount that the bank cleared the check for.  """  
      self.ClearedPerson:str = obj["ClearedPerson"]
      """  Person who cleared the check (System Set).  """  
      self.ClearedDate:str = obj["ClearedDate"]
      """  Date that the check was cleared in the system (System Set).  """  
      self.ClearedTime:str = obj["ClearedTime"]
      """  Time that the check was cleared in the system - in HH:MM:SS format (System Set).  """  
      self.ClearedStmtEndDate:str = obj["ClearedStmtEndDate"]
      """  End Date of the Statement that the check was cleared on.  """  
      self.BankSlip:str = obj["BankSlip"]
      """  The identifier of the Bankslip document (bank statement) on which this transaction was cleared by the bank. This is updated via the bank reconciliation process.  This is also written to the related GLJrnDtl records.  """  
      self.CashBookNum:int = obj["CashBookNum"]
      """  This field identifies a bankslip.  """  
      self.CashbookLine:int = obj["CashbookLine"]
      """  This field identifies a line of a bankslip.  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  Fiscal year suffix.  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  The fiscal calendar year/suffix/period were derived from.  """  
      self.PaymentNumber:str = obj["PaymentNumber"]
      """  PaymentNumber  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.ActiveToPrint:bool = obj["ActiveToPrint"]
      """  ActiveToPrint  """  
      self.MXRecDate:str = obj["MXRecDate"]
      """  MXRecDate  """  
      self.VoidedDate:str = obj["VoidedDate"]
      """  VoidedDate  """  
      self.EmpFirstName:str = obj["EmpFirstName"]
      self.EmpID:str = obj["EmpID"]
      self.EmpLastName:str = obj["EmpLastName"]
      self.EmpLinkFirstName:str = obj["EmpLinkFirstName"]
      self.EmpLinkLastName:str = obj["EmpLinkLastName"]
      self.EmpLinkName:str = obj["EmpLinkName"]
      self.EmpMiddleInit:str = obj["EmpMiddleInit"]
      self.ImageFile:str = obj["ImageFile"]
      self.IsLcked:bool = obj["IsLcked"]
      """  shows is this invoice is blocked in RvLock.  """  
      self.LockStatus:str = obj["LockStatus"]
      """  locked means can not be posted: an invoice is already in review journal or in posting process.  """  
      self.PhotoFile:str = obj["PhotoFile"]
      self.PRInterfacedContinue:bool = obj["PRInterfacedContinue"]
      """  Used in VoidPRCheck - User response to a question when GL is not interfaced.  """  
      self.RvnJrnUID:int = obj["RvnJrnUID"]
      """  Review Journal UID  """  
      self.SocSecNum:str = obj["SocSecNum"]
      self.AddressList:str = obj["AddressList"]
      self.AddressListFormatted:str = obj["AddressListFormatted"]
      """  The columns is the formatted by new line separator version of the AddressList column  """  
      self.DspCheckAmt:int = obj["DspCheckAmt"]
      """  Display CheckAmt for kinetic  """  
      self.DspCheckDate:str = obj["DspCheckDate"]
      """  Display CheckDate for kinetic  """  
      self.DspCheckNum:int = obj["DspCheckNum"]
      """  Display CheckNum for kinetic  """  
      self.BitFlag:int = obj["BitFlag"]
      self.BankAcctIDBankName:str = obj["BankAcctIDBankName"]
      self.BankAcctIDDescription:str = obj["BankAcctIDDescription"]
      self.ClassIDDescription:str = obj["ClassIDDescription"]
      self.WorkCompCodeDescription:str = obj["WorkCompCodeDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PRCheckTGLCRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.RelatedToFile:str = obj["RelatedToFile"]
      """   Identifies the master file to which the GL Control is related to.  This field is used to properly isolate controls to the masters they are related to.
For example; Customer, PartClass identifies controls that are related to Customers and Part Classes  """  
      self.Key1:str = obj["Key1"]
      """  Major component of the foreign key of the related master record. For example: For a "PORel" control this field would contain the related PO Number.  """  
      self.Key2:str = obj["Key2"]
      """   2nd component of the foreign key to the related master record.   For example: For a "PORel" control this field would contain the related PO Line Number.
The usage of this field is dependent on the type of record.  """  
      self.Key3:str = obj["Key3"]
      """  3rd component of the foreign key to the related master record.  For example: For a "PORel" control this field would contain the related PO Release Number.  The usage of this field is dependent record type.  """  
      self.Key4:str = obj["Key4"]
      """   4th component of the foreign key to the related master record.
The usage of this field is dependent record type.  """  
      self.Key5:str = obj["Key5"]
      """   5th component of the foreign key to the related master record.
The usage of this field is dependent record type.  """  
      self.Key6:str = obj["Key6"]
      """   6th component of the foreign key to the related master record.
The usage of this field is dependent record type.  """  
      self.TGLCTranNum:int = obj["TGLCTranNum"]
      """  Internal identifier used to keep records unique for the related record.  The system generates this number by finding the last TranGLC record for the RelatedToFile-Key1-Key2 etc. and adding 1 to it.  """  
      self.GLAcctContext:str = obj["GLAcctContext"]
      """  String identifier of the account context.  """  
      self.BookID:str = obj["BookID"]
      """  Reference to an accounting book.  If not blank must be a valid entry in the GLBook table.  """  
      self.COACode:str = obj["COACode"]
      """  The chart of account code used by the book.  Will contain the Master COA when BookID is blank.  Reference only.  Used for integrity checking when updating/deleting a GL account.  """  
      self.GLAccount:str = obj["GLAccount"]
      """  Full account containing the non-dynamic segment values up to 200 characters.  Unique identifier for the GL Account.  """  
      self.UserCanModify:bool = obj["UserCanModify"]
      """  Indicates if the user can update or delete this record.  """  
      self.SegValue1:str = obj["SegValue1"]
      """  Segement Value 1 of the account for this context.  """  
      self.SegValue2:str = obj["SegValue2"]
      """  Segement Value 2 of the account for this context.  """  
      self.SegValue3:str = obj["SegValue3"]
      """  Segement Value 3 of the account for this context.  """  
      self.SegValue4:str = obj["SegValue4"]
      """  Segement Value 4 of the account for this context.  """  
      self.SegValue5:str = obj["SegValue5"]
      """  Segement Value 5 of the account for this context.  """  
      self.SegValue6:str = obj["SegValue6"]
      """  Segement Value 6 of the account for this context.  """  
      self.SegValue7:str = obj["SegValue7"]
      """  Segement Value 7 of the account for this context.  """  
      self.SegValue8:str = obj["SegValue8"]
      """  Segement Value 8 of the account for this context.  """  
      self.SegValue9:str = obj["SegValue9"]
      """  Segement Value 9 of the account for this context.  """  
      self.SegValue10:str = obj["SegValue10"]
      """  Segement Value 10 of the account for this context.  """  
      self.SegValue11:str = obj["SegValue11"]
      """  Segement Value 11 of the account for this context.  """  
      self.SegValue12:str = obj["SegValue12"]
      """  Segement Value 12 of the account for this context.  """  
      self.SegValue13:str = obj["SegValue13"]
      """  Segement Value 13 of the account for this context.  """  
      self.SegValue14:str = obj["SegValue14"]
      """  Segement Value 14 of the account for this context.  """  
      self.SegValue15:str = obj["SegValue15"]
      """  Segement Value 15 of the account for this context.  """  
      self.SegValue16:str = obj["SegValue16"]
      """  Segement Value 16 of the account for this context.  """  
      self.SegValue17:str = obj["SegValue17"]
      """  Segement Value 17 of the account for this context.  """  
      self.SegValue18:str = obj["SegValue18"]
      """  Segement Value 18 of the account for this context.  """  
      self.SegValue19:str = obj["SegValue19"]
      """  Segement Value 19 of the account for this context.  """  
      self.SegValue20:str = obj["SegValue20"]
      """  Segement Value 20 of the account for this context.  """  
      self.SysGLControlType:str = obj["SysGLControlType"]
      """  Unique Identifier of the system GL Control Type.  """  
      self.SysGLControlCode:str = obj["SysGLControlCode"]
      """  System generated GL Control Identifier.  """  
      self.ExtCompanyID:str = obj["ExtCompanyID"]
      """  Global Company identifier.  Used in Multi-Company Journal.  """  
      self.IsExternalCompany:bool = obj["IsExternalCompany"]
      """  Flag to indicate the account in this record is for an external company.  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """  Fiscal year of the related GLJrnDtl.  """  
      self.JournalCode:str = obj["JournalCode"]
      """  JournalCode of the related GLJrnDtl.  """  
      self.JournalNum:int = obj["JournalNum"]
      """  Journal number of the related GLJrnDtl.  """  
      self.JournalLine:int = obj["JournalLine"]
      """  JournalLine of the related GLJrnDtl.  """  
      self.TranDate:str = obj["TranDate"]
      """  Transaction date of the transaction.  This is used in order to display the transactions in date order.  """  
      self.TranSource:str = obj["TranSource"]
      """   An internal code to identify the table of  the source transaction.
P = PartTran
L = LaborDtl
I = InvcHead
Note: The system does not combine TranSource when creating GLJrnDtl. That is, a specific GLJrnDtl record can only be related to one source.  """  
      self.LaborHedSeq:int = obj["LaborHedSeq"]
      """  LaborHedSeq of the related LaborDtl.  Pertains only to source from LaborDtl (TranSource = "L")  """  
      self.LaborDtlSeq:int = obj["LaborDtlSeq"]
      """  LaborDtlSeq of the related LaborDtl. Pertains only to source from LaborDtl (TranSource = "L")  """  
      self.SysDate:str = obj["SysDate"]
      """  System date of the related PartTran record.  Pertains only to source from PartTran (TranSource = "P")  """  
      self.SysTime:int = obj["SysTime"]
      """  System time of the related PartTran record.  Pertains only to source from PartTran (TranSource = "P")  """  
      self.TranNum:int = obj["TranNum"]
      """  TranNum of the related PartTran record.  Pertains only to source from PartTran (TranSource = "P")  """  
      self.ARInvoiceNum:int = obj["ARInvoiceNum"]
      """  InvoiceNum of the related InvcHead record.  Pertains only to source from PartTran (TranSource = "I")  """  
      self.TransAmt:int = obj["TransAmt"]
      """  Transaction amount that this transaction posted to the related GlJrnDtl.  """  
      self.InvoiceLine:int = obj["InvoiceLine"]
      """  Invoice Line Number associated with this GL Journal  """  
      self.SeqNum:int = obj["SeqNum"]
      """  The sequence number associated with this GL journal  """  
      self.VendorNum:int = obj["VendorNum"]
      """  The Internal VendorNum that ties back to the Vendor master file.  This field is not directly maintainable.  """  
      self.APInvoiceNum:str = obj["APInvoiceNum"]
      """  Vendor's invoice number.  """  
      self.CreateDate:str = obj["CreateDate"]
      """  Date record was created  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  Fiscal year suffix.  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  The fiscal calendar year/suffix/period were derived from.  """  
      self.CreditAmount:int = obj["CreditAmount"]
      """  Credit Amount.  """  
      self.DebitAmount:int = obj["DebitAmount"]
      """  Debit Amount.  """  
      self.BookCreditAmount:int = obj["BookCreditAmount"]
      """  BookCreditAmount  """  
      self.BookDebitAmount:int = obj["BookDebitAmount"]
      """  Book Debit Amount  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  A unique code that identifies the document currency.  """  
      self.RecordType:str = obj["RecordType"]
      """   Indicates if this record contains account data only or reference data such as journal number, amounts, etc.  Valid  values are:
A - account data only
R - reference data  """  
      self.CorrAccUID:int = obj["CorrAccUID"]
      """  When a posting rule creates a pair of journal details balancing each other, each detail in the pair should reference the other one. This allows to show correspondence of accounts in reports. Support of reports that allow this being visible is not in the scope of this change.  """  
      self.ABTUID:str = obj["ABTUID"]
      """  this field equals ABTUID which was created during posting  """  
      self.RuleUID:int = obj["RuleUID"]
      """  Technical identifier.  """  
      self.Statistical:int = obj["Statistical"]
      """   Identifies if statistical information may be entered for the natural (chart) account.
Accounts can be used only for monetary amounts, both monetary and statistical amounts or only for statistical amounts.
0 = Only used for monetary amounts.
1 = Used for both monetary and statistical amounts.
2 = Only used for statistical amounts.  """  
      self.StatUOMCode:str = obj["StatUOMCode"]
      """  Statistical UOM code.  """  
      self.DebitStatAmt:int = obj["DebitStatAmt"]
      """  This field shows Debit statistical amount.  """  
      self.CreditStatAmt:int = obj["CreditStatAmt"]
      """  This field shows Credit statistical amount.  """  
      self.IsModifiedByUser:bool = obj["IsModifiedByUser"]
      """  IsModifiedByUser  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.MovementNum:int = obj["MovementNum"]
      """  MovementNum  """  
      self.MovementType:str = obj["MovementType"]
      """  MovementType  """  
      self.Plant:str = obj["Plant"]
      """  Plant  """  
      self.HeadNum:int = obj["HeadNum"]
      self.BitFlag:int = obj["BitFlag"]
      self.COADescription:str = obj["COADescription"]
      self.GLAccountGLAcctDisp:str = obj["GLAccountGLAcctDisp"]
      self.GLAccountAccountDesc:str = obj["GLAccountAccountDesc"]
      self.GLAccountGLShortAcct:str = obj["GLAccountGLShortAcct"]
      self.GLBookDescription:str = obj["GLBookDescription"]
      self.GLBookCurrencyCode:str = obj["GLBookCurrencyCode"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PRChkDedRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.HeadNum:int = obj["HeadNum"]
      """  Duplicated from related PRCheck.  """  
      self.DeductionID:str = obj["DeductionID"]
      """  The deduction Id that this check deduction record is related to.  """  
      self.DeductionNum:int = obj["DeductionNum"]
      """  DeductionNum of the related PREmpDed.  """  
      self.ScheduledAmt:int = obj["ScheduledAmt"]
      """  Deduction Amount scheduled to be taken.  Calculated based on the values stored in PREmpDed. This amount includes any CarryOverAmt.  """  
      self.ManualCalc:bool = obj["ManualCalc"]
      """  Indicates if the Deduction Amount is manually calculated.  The system will not calculate the DeductionAmount when ManualCalc = Yes.  """  
      self.CalcOrder:int = obj["CalcOrder"]
      """  An internally assigned integer which controls the order in which deductions are processed. It is created/used by the payroll calculation process. It is not the same thing as the PRDeduct.Priority ! Basically it is a sequential # which was generated by processing the deductions in priority order. An exception is for negative deductions, they are set to zero (highest priority). The CalcOrder comes into play when there are insufficient funds to take all the deductions. When this occurs the deductions are decreased in a descending CalcOrder sequence until the check becomes positive.  """  
      self.DeductionAmt:int = obj["DeductionAmt"]
      """  Deduction Amount taken. Normally this is the same a ScheduledAmt, except in the case where there was insufficient pay to take the deduction. In which case this value could be lower.  """  
      self.ClassID:str = obj["ClassID"]
      """  Payroll class ID that employee is currently assigned to.  A mirror image of PREmpMas. It is kept in sync by the PREmpMas write trigger.  """  
      self.Posted:bool = obj["Posted"]
      """  Mirror image of PRCheck.Posted.  """  
      self.EmpLink:str = obj["EmpLink"]
      """  Encoded value which identifies the employee. Mirror image of PRCheck.EmpLink.  """  
      self.CheckDate:str = obj["CheckDate"]
      """  mirror image of PRCheck.CheckDate  """  
      self.PriorDedYTD:int = obj["PriorDedYTD"]
      """  Deduction Year to date amount taken.  """  
      self.Voided:bool = obj["Voided"]
      """   An internal flag indicating if this is a Void payment transaction.
This is set by the P/R void check program.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.PrintHeadNum:int = obj["PrintHeadNum"]
      """  PrintHeadNum  """  
      self.EmpID:str = obj["EmpID"]
      self.FirstName:str = obj["FirstName"]
      """  First name of employee.  """  
      self.GroupID:str = obj["GroupID"]
      self.LastName:str = obj["LastName"]
      """  Last name of employee  """  
      self.Name:str = obj["Name"]
      """  This is the employees full name. This is not directly maintainable. It is a concatenation of the FirstName + MiddleInitial + LastName fields. It exists so that it can be used in browses or where ever the complete name in a first, middle, last fashion is required.  """  
      self.Reference:str = obj["Reference"]
      self.BitFlag:int = obj["BitFlag"]
      self.ClassIDDescription:str = obj["ClassIDDescription"]
      self.DeductionIDDescription:str = obj["DeductionIDDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PRChkDtlRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.HeadNum:int = obj["HeadNum"]
      """  Duplicated from the related PRCheck.  """  
      self.LineNum:int = obj["LineNum"]
      """  Integer assigned by the system which is used as one of the fields to uniquely identify the PRChkDtl record.  """  
      self.PayrollDate:str = obj["PayrollDate"]
      """  Date that the employee worked or earned the pay.  """  
      self.PayTypeID:str = obj["PayTypeID"]
      """   Identifies the Pay type of this payment record.  A foreign key to the PayType master table.  This must be a valid PayType where PayType.PremiumFactor <= 1.00.
Ex:( Regular, Holiday, Sick, Vacation . . .)  """  
      self.PayRate:int = obj["PayRate"]
      """  The employee's base hourly pay rate.  This rate does not include premium or shift differential factors.  It is defaulted from the PREmpMas.PayRate field.  """  
      self.BaseHours:int = obj["BaseHours"]
      """   Hours for non premium time.  Maintainable only if PayTypeID is not blank.
Stored as Hours.Hundreths. For example 3 1/2 hours is stored as 3.5  """  
      self.BasePay:int = obj["BasePay"]
      """  Base pay is the pay amount calculated non-premium hours employees base pay rate.  (see PremiumPay, ShiftPay).  It is calculated as  (BaseHours * PayRate) or set = to the employee salary amount.  It can be overridden in hours entry for salaried employees.  """  
      self.PremiumPayType:str = obj["PremiumPayType"]
      """  Identifies the premium Paytype of this payment record (Ex: OT, etc.).  A foreign key to the PayType master table.  This must be a valid PayType where PayType.PremiumFactor > 1.00.  """  
      self.PremiumHours:int = obj["PremiumHours"]
      """   Hours to be paid at the premium rate.  This is stored as Hours.Hundreths. For example 3 1/2 hours is stored as 3.5
This is disabled and zero if PremiumPaytype = blank.  """  
      self.PremiumBasePay:int = obj["PremiumBasePay"]
      """   The amount paid for premium hours not including the premium amount.  Not directly maintainable. (PremiumPayHours* Payrate )
Ex: rate = $10.00,  hours = 3, PremiumBasePay = 30.00. 
The Base Pay portion of the total premium pay amount  is kept separate from the Premium Pay portion for users who wish to track the premium portion of overtime expenses separately in general ledger.  """  
      self.PremiumPay:int = obj["PremiumPay"]
      """   Premium pay is the additional amount above the base pay that is being paid as a premium for this pay type. It is not directly maintainable.
For example PayHours = 8, PayRate = 10.00 and PremiumFactor = 1.5,  BasePay would be 80.00 and PremiumPay would be 40.00.
The Base Pay is kept separate from the Premium Pay for users who wish to track the premium portion of the pay separately in general ledger.
PremiumPayHours * (Payrate * (PremiumFactor - 1.00)).  """  
      self.Shift:int = obj["Shift"]
      """   Defaults from the EmpBasic.Shift when entered through payroll hours entry, or was from LaborHed.Shift is the case the record was created from labor transfer process.
Note:  When shift is changed in check entry the pay amounts may need to be recalculated if shift pay is active.  """  
      self.ShiftPay:int = obj["ShiftPay"]
      """   Shift pay is the amount paid due to shift differential.
(BaseHours * ShiftDifferential)  + 
PremiumHours * (ShiftDifferential * PremiumFactor).
PremiumFactor  is used only if PayType.IncludeShift = Yes. 
Note: Shift differential is either an additional percentage of payrate or an additional flat amount.  
For example PayHours = 8, PayRate = 10.00 and Shift differential is an extra 1.00 per hour. ShiftPay would be $8.00.
This is refreshed when changes are made to Shift, PayRate, or PayHours or PremiumHours or PayType.  """  
      self.ClassID:str = obj["ClassID"]
      """  Payroll class ID that employee is currently assigned to. A mirror image of PREmpMas. It is kept in sync by the PREmpMas write trigger.  """  
      self.Posted:bool = obj["Posted"]
      """  Mirror image of PRCheck.Posted.  """  
      self.EmpLink:str = obj["EmpLink"]
      """  Encoded value which identifies the employee. Mirror image of PRCheck.EmpLink.  """  
      self.CheckDate:str = obj["CheckDate"]
      """  mirror image of PRCheck.CheckDate.  This is not updated until the checks are posted.  """  
      self.FromLabor:bool = obj["FromLabor"]
      """  A internally used flag which indicates that this record was generated from a LaborHed record.  """  
      self.Voided:bool = obj["Voided"]
      """   An internal flag indicating if this is a Void payment transaction.
This is set by the P/R void check program.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.PrintHeadNum:int = obj["PrintHeadNum"]
      """  PrintHeadNum  """  
      self.IsOutdatedLabor:bool = obj["IsOutdatedLabor"]
      """  IsOutdatedLabor  """  
      self.DiffMethod:str = obj["DiffMethod"]
      self.DiffMethodDesc:str = obj["DiffMethodDesc"]
      self.DiffQualifier:str = obj["DiffQualifier"]
      self.DiffQualifierDesc:str = obj["DiffQualifierDesc"]
      self.DiffRate:int = obj["DiffRate"]
      self.EmpID:str = obj["EmpID"]
      self.FirstName:str = obj["FirstName"]
      """  First name of employee.  """  
      self.GroupID:str = obj["GroupID"]
      self.LastName:str = obj["LastName"]
      """  Last name of employee  """  
      self.Name:str = obj["Name"]
      """  This is the employees full name. This is not directly maintainable. It is a concatenation of the FirstName + MiddleInitial + LastName fields. It exists so that it can be used in browses or where ever the complete name in a first, middle, last fashion is required.  """  
      self.ShiftTimesDesc:str = obj["ShiftTimesDesc"]
      self.TotalHours:int = obj["TotalHours"]
      self.TotalPay:int = obj["TotalPay"]
      self.VoidedDate:str = obj["VoidedDate"]
      """  Used in VoidPRCheck - Date the check was voided.  """  
      self.AmountType:str = obj["AmountType"]
      self.DateRange:str = obj["DateRange"]
      """   DateRange specifies the range between record is created depending of payroll frequency, the possible values are:
"Outdated", labor processed before period begins
"In Pay Range", labor processed between perido begin and period ending
"Outrunning". labor processed after period ending  """  
      self.BitFlag:int = obj["BitFlag"]
      self.ClassIDDescription:str = obj["ClassIDDescription"]
      self.PayTypeIDDescription:str = obj["PayTypeIDDescription"]
      self.PremiumPayTypeIDDescription:str = obj["PremiumPayTypeIDDescription"]
      self.ShiftDescription:str = obj["ShiftDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PRChkTaxRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.HeadNum:int = obj["HeadNum"]
      """  Duplicated from related PRCheck.  """  
      self.TaxTblID:str = obj["TaxTblID"]
      """  Tax Table ID  """  
      self.TaxType:str = obj["TaxType"]
      """  Identifies the type of tax table.  Valid values are "FIT" - Federal, "SIT" - State, "FUTA" - Federal Unemployment, "SUTA" - State Unemployment,  "SS" - Social Security, "MED" - Medicare, "CITY" - Local, "CNTY" - County, "OTHR" - Other.  """  
      self.ClassID:str = obj["ClassID"]
      """  Payroll class ID that employee is currently assigned to. A mirror image of PREmpMas. It is kept in sync by the PREmpMas write trigger.  """  
      self.Posted:bool = obj["Posted"]
      """  Mirror image of PRCheck.Posted.  """  
      self.EmpLink:str = obj["EmpLink"]
      """  Encoded value which identifies the employee. Mirror image of PRCheck.EmpLink.  """  
      self.CheckDate:str = obj["CheckDate"]
      """  mirror image of PRCheck.CheckDate  """  
      self.TaxAmt:int = obj["TaxAmt"]
      """  Amount withheld on this check for a specific tax.  """  
      self.PriorTaxYTD:int = obj["PriorTaxYTD"]
      """  The Year to Date tax withheld  prior to this check. Current YTD is PriorTaxYTD + TaxAmt.  """  
      self.TaxableHours:int = obj["TaxableHours"]
      """  Taxable hours on this check for the tax jurisdiction.  This is the BaseHours and PremiumHours if the PayType is not exempt from the tax jurisdiction.  """  
      self.SupTaxableAmt:int = obj["SupTaxableAmt"]
      """  The taxable amount of supplemental pay for this check  for the tax jurisdiction.  """  
      self.SupTaxableHours:int = obj["SupTaxableHours"]
      """  The hours accumulated from supplemental pay records.  This is used in tax calc when tax basis is % of hours.  """  
      self.TaxableAmt:int = obj["TaxableAmt"]
      """  Pay check amount that is considered as taxable for this tax jurisdiction. This is calculated by the system as part of the payroll calculate routine.  """  
      self.PriorTaxableYTD:int = obj["PriorTaxableYTD"]
      """  The Year to Date taxable amount prior to this check. Current YTD is PriorTaxableYTD + TaxableAmt.  """  
      self.Active:bool = obj["Active"]
      """  Indicates if this tax record for the check is taxable as of the check date. Of course, if a tax was first taken it would have been taxable. This flag is used so that if after the check is posted it is discovered that it was taken in error the user can set this to NO which would reduce the year to date taxable amount from this date forward. This situation should not be a common occurrence; however it's more likely when employees' have multiple taxes that are deactivated/activated during the same year. It does not change the Tax withheld only taxable.  This flag is needed so that the "Recalculate" taxable amounts would work correctly.  """  
      self.ManualCalc:bool = obj["ManualCalc"]
      """  Indicates if the Tax Amount is manually calculated.  The system will not calculate the TaxAmount when ManualCalc = Yes.  """  
      self.Voided:bool = obj["Voided"]
      """   An internal flag indicating if this is a Void payment transaction.
This is set by the P/R void check program.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.PrintHeadNum:int = obj["PrintHeadNum"]
      """  PrintHeadNum  """  
      self.CreditAmount:int = obj["CreditAmount"]
      self.EmpID:str = obj["EmpID"]
      self.FilingStatus:str = obj["FilingStatus"]
      self.FirstName:str = obj["FirstName"]
      """  First name of employee.  """  
      self.GroupID:str = obj["GroupID"]
      self.LastName:str = obj["LastName"]
      """  Last name of employee  """  
      self.Name:str = obj["Name"]
      """  This is the employees full name. This is not directly maintainable. It is a concatenation of the FirstName + MiddleInitial + LastName fields. It exists so that it can be used in browses or where ever the complete name in a first, middle, last fashion is required.  """  
      self.TaxDesc:str = obj["TaxDesc"]
      self.BitFlag:int = obj["BitFlag"]
      self.ClassIDDescription:str = obj["ClassIDDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class CalculateDeductsAndTaxes_input:
   """ Required : 
   GroupID
   HeadNum
   ds
   """  
   def __init__(self, obj):
      self.GroupID:str = obj["GroupID"]
      """  The group id to calculate deductions and taxes for  """  
      self.HeadNum:int = obj["HeadNum"]
      """  The current PRCheck.HeadNum record.  Is used to
            rebuild the dataset so the data is current  """  
      self.ds:list[Erp_Tablesets_PayrollCheckEntryTableset] = obj["ds"]
      pass

class CalculateDeductsAndTaxes_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PayrollCheckEntryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class CalculateOvertimeVerification_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.VerificationMsg:str = obj["parameters"]
      pass

      """  output parameters  """  

class CalculateOvertime_input:
   """ Required : 
   GroupID
   HeadNum
   ds
   """  
   def __init__(self, obj):
      self.GroupID:str = obj["GroupID"]
      """  The group id to calculate overtime for  """  
      self.HeadNum:int = obj["HeadNum"]
      """  The current PRCheck.HeadNum record.  Is used to
            rebuild the dataset so the data is current  """  
      self.ds:list[Erp_Tablesets_PayrollCheckEntryTableset] = obj["ds"]
      pass

class CalculateOvertime_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PayrollCheckEntryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangePRCheckEmpID_input:
   """ Required : 
   ProposedEmpID
   ds
   """  
   def __init__(self, obj):
      self.ProposedEmpID:str = obj["ProposedEmpID"]
      """  The proposed employee id  """  
      self.ds:list[Erp_Tablesets_PayrollCheckEntryTableset] = obj["ds"]
      pass

class ChangePRCheckEmpID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PayrollCheckEntryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangePRChkDtlAmountType_input:
   """ Required : 
   PRChkDtlKey
   ProposedAmountType
   ds
   """  
   def __init__(self, obj):
      self.PRChkDtlKey:str = obj["PRChkDtlKey"]
      """  PRChkDtl Key of row to update ProposedBaseHours Company/HeadNum/LineNum  """  
      self.ProposedAmountType:str = obj["ProposedAmountType"]
      """  The proposed amount type  """  
      self.ds:list[Erp_Tablesets_PayrollCheckEntryTableset] = obj["ds"]
      pass

class ChangePRChkDtlAmountType_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PayrollCheckEntryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangePRChkDtlBaseHours_input:
   """ Required : 
   PRChkDtlKey
   ProposedBaseHours
   ds
   """  
   def __init__(self, obj):
      self.PRChkDtlKey:str = obj["PRChkDtlKey"]
      """  PRChkDtl Key of row to update ProposedBaseHours Company/HeadNum/LineNum  """  
      self.ProposedBaseHours:int = obj["ProposedBaseHours"]
      """  The proposed base hours  """  
      self.ds:list[Erp_Tablesets_PayrollCheckEntryTableset] = obj["ds"]
      pass

class ChangePRChkDtlBaseHours_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PayrollCheckEntryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangePRChkDtlBasePay_input:
   """ Required : 
   ProposedBasePay
   ds
   """  
   def __init__(self, obj):
      self.ProposedBasePay:int = obj["ProposedBasePay"]
      """  The proposed base pay amount  """  
      self.ds:list[Erp_Tablesets_PayrollCheckEntryTableset] = obj["ds"]
      pass

class ChangePRChkDtlBasePay_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PayrollCheckEntryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangePRChkDtlPayRate_input:
   """ Required : 
   PRChkDtlKey
   ProposedPayRate
   ds
   """  
   def __init__(self, obj):
      self.PRChkDtlKey:str = obj["PRChkDtlKey"]
      """  PRChkDtl Key of row to update ProposedBaseHours Company/HeadNum/LineNum  """  
      self.ProposedPayRate:int = obj["ProposedPayRate"]
      """  The proposed pay rate  """  
      self.ds:list[Erp_Tablesets_PayrollCheckEntryTableset] = obj["ds"]
      pass

class ChangePRChkDtlPayRate_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PayrollCheckEntryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangePRChkDtlPayTypeID_input:
   """ Required : 
   PRChkDtlKey
   ProposedPayTypeID
   ds
   """  
   def __init__(self, obj):
      self.PRChkDtlKey:str = obj["PRChkDtlKey"]
      """  PRChkDtl Key of row to update ProposedBaseHours Company/HeadNum/LineNum  """  
      self.ProposedPayTypeID:str = obj["ProposedPayTypeID"]
      """  The proposed pay type id  """  
      self.ds:list[Erp_Tablesets_PayrollCheckEntryTableset] = obj["ds"]
      pass

class ChangePRChkDtlPayTypeID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PayrollCheckEntryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangePRChkDtlPayrollDate_input:
   """ Required : 
   ProposedPayrollDate
   ds
   """  
   def __init__(self, obj):
      self.ProposedPayrollDate:str = obj["ProposedPayrollDate"]
      """  The proposed payroll date  """  
      self.ds:list[Erp_Tablesets_PayrollCheckEntryTableset] = obj["ds"]
      pass

class ChangePRChkDtlPayrollDate_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PayrollCheckEntryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangePRChkDtlPremiumHours_input:
   """ Required : 
   PRChkDtlKey
   ProposedPremiumHours
   ds
   """  
   def __init__(self, obj):
      self.PRChkDtlKey:str = obj["PRChkDtlKey"]
      """  PRChkDtl Key of row to update ProposedBaseHours Company/HeadNum/LineNum  """  
      self.ProposedPremiumHours:int = obj["ProposedPremiumHours"]
      """  The proposed premium hours  """  
      self.ds:list[Erp_Tablesets_PayrollCheckEntryTableset] = obj["ds"]
      pass

class ChangePRChkDtlPremiumHours_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PayrollCheckEntryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangePRChkDtlPremiumPayType_input:
   """ Required : 
   PRChkDtlKey
   ProposedPremiumPayType
   ds
   """  
   def __init__(self, obj):
      self.PRChkDtlKey:str = obj["PRChkDtlKey"]
      """  PRChkDtl Key of row to update ProposedBaseHours Company/HeadNum/LineNum  """  
      self.ProposedPremiumPayType:str = obj["ProposedPremiumPayType"]
      """  The proposed premium pay type id  """  
      self.ds:list[Erp_Tablesets_PayrollCheckEntryTableset] = obj["ds"]
      pass

class ChangePRChkDtlPremiumPayType_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PayrollCheckEntryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangePRChkDtlShift_input:
   """ Required : 
   PRChkDtlKey
   ProposedShift
   ds
   """  
   def __init__(self, obj):
      self.PRChkDtlKey:str = obj["PRChkDtlKey"]
      """  PRChkDtl Key of row to update ProposedBaseHours Company/HeadNum/LineNum  """  
      self.ProposedShift:int = obj["ProposedShift"]
      """  The proposed shift  """  
      self.ds:list[Erp_Tablesets_PayrollCheckEntryTableset] = obj["ds"]
      pass

class ChangePRChkDtlShift_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PayrollCheckEntryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class CheckDocumentIsLocked_input:
   """ Required : 
   keyValue
   """  
   def __init__(self, obj):
      self.keyValue:str = obj["keyValue"]
      """  HeadNum  """  
      pass

class CheckDocumentIsLocked_output:
   def __init__(self, obj):
      pass

class CheckPrinted_input:
   """ Required : 
   GroupID
   """  
   def __init__(self, obj):
      self.GroupID:str = obj["GroupID"]
      """  The group id the check is assigned to  """  
      pass

class CheckPrinted_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.QuestionText:str = obj["parameters"]
      pass

      """  output parameters  """  

class DeleteByID_input:
   """ Required : 
   headNum
   """  
   def __init__(self, obj):
      self.headNum:int = obj["headNum"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class ElecFileDownloaded_input:
   """ Required : 
   GroupID
   """  
   def __init__(self, obj):
      self.GroupID:str = obj["GroupID"]
      """  The group id the check is assigned to  """  
      pass

class ElecFileDownloaded_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.QuestionText:str = obj["parameters"]
      pass

      """  output parameters  """  

class Erp_Tablesets_PRCheckListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.Posted:bool = obj["Posted"]
      """  An internal flag which indicates if this check has been Posted.  If "NO" then it is  considered as still being in the data entry mode. In which case it is still accessible by the check entry programs.  It is set to "Yes" by the posting process.  """  
      self.GroupID:str = obj["GroupID"]
      """  The data entry "Group" that the check belongs to.  All checks belong to a "Group."  It is assigned to the record during creation using the "current group" that the user is signed into.  It cannot be changed.  The GroupID is used to selectively print and post.  """  
      self.HeadNum:int = obj["HeadNum"]
      """  An integer automatically assigned by the system using the database sequence called "PRCheckSeq".  HeadNum + Company creates a unique key for the record. This is for internal control only the user never needs to reference.  """  
      self.EmpLink:str = obj["EmpLink"]
      """  Encoded value which identifies the employee.  """  
      self.BankAcctID:str = obj["BankAcctID"]
      """  BankAcctId of the BankAcct master that this check was drawn  against. This field is updated during the check printing process for system printed checks or entered by the user for manually printed checks. It must be entered and valid for manual checks. It is invalid if not found or BankAcct.Active = No.  """  
      self.CheckNum:int = obj["CheckNum"]
      """  Check number is assigned during the check printing process for checks that are printed by the system or entered by the user for hand written checks. NOTE:  Posting of the group is not allowed if any CheckHed record exits with a zero check.  """  
      self.CheckDate:str = obj["CheckDate"]
      """  Check Date is assigned during the printing process for system printed checks or entered by the user for hand written checks.  """  
      self.PSDate:str = obj["PSDate"]
      """  Pay period start date for this check.  This is updated as part of the payroll posting process for system generated checks.  It is entered by the user for manual checks.  """  
      self.PEDate:str = obj["PEDate"]
      """  Pay period end date for this check.  This is updated as part of the payroll posting process for system generated checks.  It is entered by the user for manual checks.  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """  Fiscal Year that the check is posted to.  Updated during the check printing process for system printed checks or updated based on the CheckDate for hand written checks.  """  
      self.FiscalPeriod:int = obj["FiscalPeriod"]
      """  G/L fiscal period that this check is posted to.  Updated by the check printing process for system printed checks.  For hand written checks it updated by check entry program based on the check date.  """  
      self.Voided:bool = obj["Voided"]
      """  Voided flag  """  
      self.TotalBasePay:int = obj["TotalBasePay"]
      """  Total Base Pay for this check. Not user maintainable.  It summarizes all PRChkDtl for the check.  Updated via PRChkDtl write/delete triggers. The triggers update this with  (BasePay + PremiumPay + PremiumBasePay + ShiftPay)  """  
      self.TotalPremiumPay:int = obj["TotalPremiumPay"]
      """  Total Premium Pay for this check.  Not user maintainable.  It summarizes all PRChkDtl.PremiumPay for the check.  Updated via PRChkDtl write/delete triggers.  """  
      self.TotalShiftPay:int = obj["TotalShiftPay"]
      """  Total Shift Pay for this check.  Not user maintainable.  It summarizes all PRChkDtl.ShiftPay for the check.  Updated via PRChkDtl write/delete triggers.  """  
      self.TotalTaxes:int = obj["TotalTaxes"]
      """  Total of all Tax amounts for the check.  Not user maintainable.  It summarizes all PRChkTax.TaxAmt for the check.  Updated via PRChkTax write/delete triggers.  """  
      self.TotalDeductions:int = obj["TotalDeductions"]
      """  Total of all deduction amounts for the check.  Not user maintainable.  It summarizes all PRChkDed.DeductionAmt for the check.  Updated via PRChkDed write/delete triggers.  """  
      self.TotalBaseHours:int = obj["TotalBaseHours"]
      """  Total Base Hours on this check. Not directly maintainable by user. A summary of PRChkDtl.BaseHours updated via the PRChkDtl write/delete triggers  """  
      self.TotalPremiumHours:int = obj["TotalPremiumHours"]
      """  Total Premium Hours on this check. Not directly maintainable by user. A summary of PRChkDtl.PremiumHours updated via the PRChkDtl write/delete triggers  """  
      self.CheckAmt:int = obj["CheckAmt"]
      """  Net Check Amount.  Not directly user maintainable.  Updated as (PRCheck.TotalBasePay + TotalPremiumPay + ShiftPay + NonTaxAmt) - (TotalTaxes + TotalDeductions).  Updated via write trigger on PRCheck.  """  
      self.StartupCheck:bool = obj["StartupCheck"]
      """  Indicates that the check was created using the YTD Startup routines.  This is not a real check.  """  
      self.EntryPerson:str = obj["EntryPerson"]
      """  UserID that created the Check. Assign by the system using the current UserID at the time the record was created.  """  
      self.WorkCompCode:str = obj["WorkCompCode"]
      """  The WorkCompCode relates this check to the proper WorkComp master.  Used in the Worker's Comp report.  It is duplicated from the PREmpMas.WorkCompCode during the posting process.  """  
      self.ClassID:str = obj["ClassID"]
      """  Payroll class ID that employee is currently assigned to. A mirror image of PREmpMas. It is kept in sync by the PREmpMas write trigger.  """  
      self.Note:str = obj["Note"]
      """  A short note which is printed on the check.  """  
      self.PayFrequency:str = obj["PayFrequency"]
      """  Copied from PREmpMas at the time the PRCheck record is created.  """  
      self.ClearedCheck:bool = obj["ClearedCheck"]
      """  Indicates the check's cleared status.  When the Bank Statement is posted all Pending Transactions and Checks are flagged as Cleared and any variances are posted to the Bank Account's Cash and Cleared Variance Accounts.  """  
      self.ClearedPending:bool = obj["ClearedPending"]
      """  Indicates that the check is in the process of being cleared.  When the Bank Statement is posted all Pending Transactions and Checks are flagged as Cleared and any variances are posted to the Bank Account's Cash and Cleared Variance Accounts.  """  
      self.ClearedAmt:int = obj["ClearedAmt"]
      """  Amount that the bank cleared the check for.  """  
      self.ClearedPerson:str = obj["ClearedPerson"]
      """  Person who cleared the check (System Set).  """  
      self.ClearedDate:str = obj["ClearedDate"]
      """  Date that the check was cleared in the system (System Set).  """  
      self.ClearedTime:str = obj["ClearedTime"]
      """  Time that the check was cleared in the system - in HH:MM:SS format (System Set).  """  
      self.ClearedStmtEndDate:str = obj["ClearedStmtEndDate"]
      """  End Date of the Statement that the check was cleared on.  """  
      self.BankSlip:str = obj["BankSlip"]
      """  The identifier of the Bankslip document (bank statement) on which this transaction was cleared by the bank. This is updated via the bank reconciliation process.  This is also written to the related GLJrnDtl records.  """  
      self.CashBookNum:int = obj["CashBookNum"]
      """  This field identifies a bankslip.  """  
      self.CashbookLine:int = obj["CashbookLine"]
      """  This field identifies a line of a bankslip.  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  Fiscal year suffix.  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  The fiscal calendar year/suffix/period were derived from.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.MXRecDate:str = obj["MXRecDate"]
      """  MXRecDate  """  
      self.VoidedDate:str = obj["VoidedDate"]
      """  VoidedDate  """  
      self.SocSecNum:str = obj["SocSecNum"]
      self.EmpID:str = obj["EmpID"]
      self.AddressList:str = obj["AddressList"]
      self.EmpFirstName:str = obj["EmpFirstName"]
      self.EmpMiddleInit:str = obj["EmpMiddleInit"]
      self.EmpLastName:str = obj["EmpLastName"]
      self.PhotoFile:str = obj["PhotoFile"]
      self.ImageFile:str = obj["ImageFile"]
      self.PRInterfacedContinue:bool = obj["PRInterfacedContinue"]
      """  Used in VoidPRCheck - User response to a question when GL is not interfaced.  """  
      self.EmpLinkFirstName:str = obj["EmpLinkFirstName"]
      self.EmpLinkLastName:str = obj["EmpLinkLastName"]
      self.EmpLinkName:str = obj["EmpLinkName"]
      self.IsLcked:bool = obj["IsLcked"]
      """  shows is this invoice is blocked in RvLock.  """  
      self.RvnJrnUID:int = obj["RvnJrnUID"]
      """  Review Journal UID  """  
      self.LockStatus:str = obj["LockStatus"]
      """  locked means can not be posted: an invoice is already in review journal or in posting process.  """  
      self.BankAcctIDDescription:str = obj["BankAcctIDDescription"]
      """  Full description of the bank account.  """  
      self.BankAcctIDBankName:str = obj["BankAcctIDBankName"]
      """  The Bank's full name.  """  
      self.ClassIDDescription:str = obj["ClassIDDescription"]
      """  Full description of the payroll class.  """  
      self.WorkCompCodeDescription:str = obj["WorkCompCodeDescription"]
      """  Description of the workers' compensation code.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PRCheckListTableset:
   def __init__(self, obj):
      self.PRCheckList:list[Erp_Tablesets_PRCheckListRow] = obj["PRCheckList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_PRCheckRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.Posted:bool = obj["Posted"]
      """  An internal flag which indicates if this check has been Posted.  If "NO" then it is  considered as still being in the data entry mode. In which case it is still accessible by the check entry programs.  It is set to "Yes" by the posting process.  """  
      self.GroupID:str = obj["GroupID"]
      """  The data entry "Group" that the check belongs to.  All checks belong to a "Group."  It is assigned to the record during creation using the "current group" that the user is signed into.  It cannot be changed.  The GroupID is used to selectively print and post.  """  
      self.HeadNum:int = obj["HeadNum"]
      """  An integer automatically assigned by the system using the database sequence called "PRCheckSeq".  HeadNum + Company creates a unique key for the record. This is for internal control only the user never needs to reference.  """  
      self.EmpLink:str = obj["EmpLink"]
      """  Encoded value which identifies the employee.  """  
      self.BankAcctID:str = obj["BankAcctID"]
      """  BankAcctId of the BankAcct master that this check was drawn  against. This field is updated during the check printing process for system printed checks or entered by the user for manually printed checks. It must be entered and valid for manual checks. It is invalid if not found or BankAcct.Active = No.  """  
      self.CheckNum:int = obj["CheckNum"]
      """  Check number is assigned during the check printing process for checks that are printed by the system or entered by the user for hand written checks. NOTE:  Posting of the group is not allowed if any CheckHed record exits with a zero check.  """  
      self.CheckDate:str = obj["CheckDate"]
      """  Check Date is assigned during the printing process for system printed checks or entered by the user for hand written checks.  """  
      self.PSDate:str = obj["PSDate"]
      """  Pay period start date for this check.  This is updated as part of the payroll posting process for system generated checks.  It is entered by the user for manual checks.  """  
      self.PEDate:str = obj["PEDate"]
      """  Pay period end date for this check.  This is updated as part of the payroll posting process for system generated checks.  It is entered by the user for manual checks.  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """  Fiscal Year that the check is posted to.  Updated during the check printing process for system printed checks or updated based on the CheckDate for hand written checks.  """  
      self.FiscalPeriod:int = obj["FiscalPeriod"]
      """  G/L fiscal period that this check is posted to.  Updated by the check printing process for system printed checks.  For hand written checks it updated by check entry program based on the check date.  """  
      self.Voided:bool = obj["Voided"]
      """  Voided flag  """  
      self.TotalBasePay:int = obj["TotalBasePay"]
      """  Total Base Pay for this check. Not user maintainable.  It summarizes all PRChkDtl for the check.  Updated via PRChkDtl write/delete triggers. The triggers update this with  (BasePay + PremiumPay + PremiumBasePay + ShiftPay)  """  
      self.TotalPremiumPay:int = obj["TotalPremiumPay"]
      """  Total Premium Pay for this check.  Not user maintainable.  It summarizes all PRChkDtl.PremiumPay for the check.  Updated via PRChkDtl write/delete triggers.  """  
      self.TotalShiftPay:int = obj["TotalShiftPay"]
      """  Total Shift Pay for this check.  Not user maintainable.  It summarizes all PRChkDtl.ShiftPay for the check.  Updated via PRChkDtl write/delete triggers.  """  
      self.TotalTaxes:int = obj["TotalTaxes"]
      """  Total of all Tax amounts for the check.  Not user maintainable.  It summarizes all PRChkTax.TaxAmt for the check.  Updated via PRChkTax write/delete triggers.  """  
      self.TotalDeductions:int = obj["TotalDeductions"]
      """  Total of all deduction amounts for the check.  Not user maintainable.  It summarizes all PRChkDed.DeductionAmt for the check.  Updated via PRChkDed write/delete triggers.  """  
      self.TotalBaseHours:int = obj["TotalBaseHours"]
      """  Total Base Hours on this check. Not directly maintainable by user. A summary of PRChkDtl.BaseHours updated via the PRChkDtl write/delete triggers  """  
      self.TotalPremiumHours:int = obj["TotalPremiumHours"]
      """  Total Premium Hours on this check. Not directly maintainable by user. A summary of PRChkDtl.PremiumHours updated via the PRChkDtl write/delete triggers  """  
      self.CheckAmt:int = obj["CheckAmt"]
      """  Net Check Amount.  Not directly user maintainable.  Updated as (PRCheck.TotalBasePay + TotalPremiumPay + ShiftPay + NonTaxAmt) - (TotalTaxes + TotalDeductions).  Updated via write trigger on PRCheck.  """  
      self.StartupCheck:bool = obj["StartupCheck"]
      """  Indicates that the check was created using the YTD Startup routines.  This is not a real check.  """  
      self.EntryPerson:str = obj["EntryPerson"]
      """  UserID that created the Check. Assign by the system using the current UserID at the time the record was created.  """  
      self.WorkCompCode:str = obj["WorkCompCode"]
      """  The WorkCompCode relates this check to the proper WorkComp master.  Used in the Worker's Comp report.  It is duplicated from the PREmpMas.WorkCompCode during the posting process.  """  
      self.ClassID:str = obj["ClassID"]
      """  Payroll class ID that employee is currently assigned to. A mirror image of PREmpMas. It is kept in sync by the PREmpMas write trigger.  """  
      self.Note:str = obj["Note"]
      """  A short note which is printed on the check.  """  
      self.PayFrequency:str = obj["PayFrequency"]
      """  Copied from PREmpMas at the time the PRCheck record is created.  """  
      self.ClearedCheck:bool = obj["ClearedCheck"]
      """  Indicates the check's cleared status.  When the Bank Statement is posted all Pending Transactions and Checks are flagged as Cleared and any variances are posted to the Bank Account's Cash and Cleared Variance Accounts.  """  
      self.ClearedPending:bool = obj["ClearedPending"]
      """  Indicates that the check is in the process of being cleared.  When the Bank Statement is posted all Pending Transactions and Checks are flagged as Cleared and any variances are posted to the Bank Account's Cash and Cleared Variance Accounts.  """  
      self.ClearedAmt:int = obj["ClearedAmt"]
      """  Amount that the bank cleared the check for.  """  
      self.ClearedPerson:str = obj["ClearedPerson"]
      """  Person who cleared the check (System Set).  """  
      self.ClearedDate:str = obj["ClearedDate"]
      """  Date that the check was cleared in the system (System Set).  """  
      self.ClearedTime:str = obj["ClearedTime"]
      """  Time that the check was cleared in the system - in HH:MM:SS format (System Set).  """  
      self.ClearedStmtEndDate:str = obj["ClearedStmtEndDate"]
      """  End Date of the Statement that the check was cleared on.  """  
      self.BankSlip:str = obj["BankSlip"]
      """  The identifier of the Bankslip document (bank statement) on which this transaction was cleared by the bank. This is updated via the bank reconciliation process.  This is also written to the related GLJrnDtl records.  """  
      self.CashBookNum:int = obj["CashBookNum"]
      """  This field identifies a bankslip.  """  
      self.CashbookLine:int = obj["CashbookLine"]
      """  This field identifies a line of a bankslip.  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  Fiscal year suffix.  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  The fiscal calendar year/suffix/period were derived from.  """  
      self.PaymentNumber:str = obj["PaymentNumber"]
      """  PaymentNumber  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.ActiveToPrint:bool = obj["ActiveToPrint"]
      """  ActiveToPrint  """  
      self.MXRecDate:str = obj["MXRecDate"]
      """  MXRecDate  """  
      self.VoidedDate:str = obj["VoidedDate"]
      """  VoidedDate  """  
      self.EmpFirstName:str = obj["EmpFirstName"]
      self.EmpID:str = obj["EmpID"]
      self.EmpLastName:str = obj["EmpLastName"]
      self.EmpLinkFirstName:str = obj["EmpLinkFirstName"]
      self.EmpLinkLastName:str = obj["EmpLinkLastName"]
      self.EmpLinkName:str = obj["EmpLinkName"]
      self.EmpMiddleInit:str = obj["EmpMiddleInit"]
      self.ImageFile:str = obj["ImageFile"]
      self.IsLcked:bool = obj["IsLcked"]
      """  shows is this invoice is blocked in RvLock.  """  
      self.LockStatus:str = obj["LockStatus"]
      """  locked means can not be posted: an invoice is already in review journal or in posting process.  """  
      self.PhotoFile:str = obj["PhotoFile"]
      self.PRInterfacedContinue:bool = obj["PRInterfacedContinue"]
      """  Used in VoidPRCheck - User response to a question when GL is not interfaced.  """  
      self.RvnJrnUID:int = obj["RvnJrnUID"]
      """  Review Journal UID  """  
      self.SocSecNum:str = obj["SocSecNum"]
      self.AddressList:str = obj["AddressList"]
      self.AddressListFormatted:str = obj["AddressListFormatted"]
      """  The columns is the formatted by new line separator version of the AddressList column  """  
      self.DspCheckAmt:int = obj["DspCheckAmt"]
      """  Display CheckAmt for kinetic  """  
      self.DspCheckDate:str = obj["DspCheckDate"]
      """  Display CheckDate for kinetic  """  
      self.DspCheckNum:int = obj["DspCheckNum"]
      """  Display CheckNum for kinetic  """  
      self.BitFlag:int = obj["BitFlag"]
      self.BankAcctIDBankName:str = obj["BankAcctIDBankName"]
      self.BankAcctIDDescription:str = obj["BankAcctIDDescription"]
      self.ClassIDDescription:str = obj["ClassIDDescription"]
      self.WorkCompCodeDescription:str = obj["WorkCompCodeDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PRCheckTGLCRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.RelatedToFile:str = obj["RelatedToFile"]
      """   Identifies the master file to which the GL Control is related to.  This field is used to properly isolate controls to the masters they are related to.
For example; Customer, PartClass identifies controls that are related to Customers and Part Classes  """  
      self.Key1:str = obj["Key1"]
      """  Major component of the foreign key of the related master record. For example: For a "PORel" control this field would contain the related PO Number.  """  
      self.Key2:str = obj["Key2"]
      """   2nd component of the foreign key to the related master record.   For example: For a "PORel" control this field would contain the related PO Line Number.
The usage of this field is dependent on the type of record.  """  
      self.Key3:str = obj["Key3"]
      """  3rd component of the foreign key to the related master record.  For example: For a "PORel" control this field would contain the related PO Release Number.  The usage of this field is dependent record type.  """  
      self.Key4:str = obj["Key4"]
      """   4th component of the foreign key to the related master record.
The usage of this field is dependent record type.  """  
      self.Key5:str = obj["Key5"]
      """   5th component of the foreign key to the related master record.
The usage of this field is dependent record type.  """  
      self.Key6:str = obj["Key6"]
      """   6th component of the foreign key to the related master record.
The usage of this field is dependent record type.  """  
      self.TGLCTranNum:int = obj["TGLCTranNum"]
      """  Internal identifier used to keep records unique for the related record.  The system generates this number by finding the last TranGLC record for the RelatedToFile-Key1-Key2 etc. and adding 1 to it.  """  
      self.GLAcctContext:str = obj["GLAcctContext"]
      """  String identifier of the account context.  """  
      self.BookID:str = obj["BookID"]
      """  Reference to an accounting book.  If not blank must be a valid entry in the GLBook table.  """  
      self.COACode:str = obj["COACode"]
      """  The chart of account code used by the book.  Will contain the Master COA when BookID is blank.  Reference only.  Used for integrity checking when updating/deleting a GL account.  """  
      self.GLAccount:str = obj["GLAccount"]
      """  Full account containing the non-dynamic segment values up to 200 characters.  Unique identifier for the GL Account.  """  
      self.UserCanModify:bool = obj["UserCanModify"]
      """  Indicates if the user can update or delete this record.  """  
      self.SegValue1:str = obj["SegValue1"]
      """  Segement Value 1 of the account for this context.  """  
      self.SegValue2:str = obj["SegValue2"]
      """  Segement Value 2 of the account for this context.  """  
      self.SegValue3:str = obj["SegValue3"]
      """  Segement Value 3 of the account for this context.  """  
      self.SegValue4:str = obj["SegValue4"]
      """  Segement Value 4 of the account for this context.  """  
      self.SegValue5:str = obj["SegValue5"]
      """  Segement Value 5 of the account for this context.  """  
      self.SegValue6:str = obj["SegValue6"]
      """  Segement Value 6 of the account for this context.  """  
      self.SegValue7:str = obj["SegValue7"]
      """  Segement Value 7 of the account for this context.  """  
      self.SegValue8:str = obj["SegValue8"]
      """  Segement Value 8 of the account for this context.  """  
      self.SegValue9:str = obj["SegValue9"]
      """  Segement Value 9 of the account for this context.  """  
      self.SegValue10:str = obj["SegValue10"]
      """  Segement Value 10 of the account for this context.  """  
      self.SegValue11:str = obj["SegValue11"]
      """  Segement Value 11 of the account for this context.  """  
      self.SegValue12:str = obj["SegValue12"]
      """  Segement Value 12 of the account for this context.  """  
      self.SegValue13:str = obj["SegValue13"]
      """  Segement Value 13 of the account for this context.  """  
      self.SegValue14:str = obj["SegValue14"]
      """  Segement Value 14 of the account for this context.  """  
      self.SegValue15:str = obj["SegValue15"]
      """  Segement Value 15 of the account for this context.  """  
      self.SegValue16:str = obj["SegValue16"]
      """  Segement Value 16 of the account for this context.  """  
      self.SegValue17:str = obj["SegValue17"]
      """  Segement Value 17 of the account for this context.  """  
      self.SegValue18:str = obj["SegValue18"]
      """  Segement Value 18 of the account for this context.  """  
      self.SegValue19:str = obj["SegValue19"]
      """  Segement Value 19 of the account for this context.  """  
      self.SegValue20:str = obj["SegValue20"]
      """  Segement Value 20 of the account for this context.  """  
      self.SysGLControlType:str = obj["SysGLControlType"]
      """  Unique Identifier of the system GL Control Type.  """  
      self.SysGLControlCode:str = obj["SysGLControlCode"]
      """  System generated GL Control Identifier.  """  
      self.ExtCompanyID:str = obj["ExtCompanyID"]
      """  Global Company identifier.  Used in Multi-Company Journal.  """  
      self.IsExternalCompany:bool = obj["IsExternalCompany"]
      """  Flag to indicate the account in this record is for an external company.  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """  Fiscal year of the related GLJrnDtl.  """  
      self.JournalCode:str = obj["JournalCode"]
      """  JournalCode of the related GLJrnDtl.  """  
      self.JournalNum:int = obj["JournalNum"]
      """  Journal number of the related GLJrnDtl.  """  
      self.JournalLine:int = obj["JournalLine"]
      """  JournalLine of the related GLJrnDtl.  """  
      self.TranDate:str = obj["TranDate"]
      """  Transaction date of the transaction.  This is used in order to display the transactions in date order.  """  
      self.TranSource:str = obj["TranSource"]
      """   An internal code to identify the table of  the source transaction.
P = PartTran
L = LaborDtl
I = InvcHead
Note: The system does not combine TranSource when creating GLJrnDtl. That is, a specific GLJrnDtl record can only be related to one source.  """  
      self.LaborHedSeq:int = obj["LaborHedSeq"]
      """  LaborHedSeq of the related LaborDtl.  Pertains only to source from LaborDtl (TranSource = "L")  """  
      self.LaborDtlSeq:int = obj["LaborDtlSeq"]
      """  LaborDtlSeq of the related LaborDtl. Pertains only to source from LaborDtl (TranSource = "L")  """  
      self.SysDate:str = obj["SysDate"]
      """  System date of the related PartTran record.  Pertains only to source from PartTran (TranSource = "P")  """  
      self.SysTime:int = obj["SysTime"]
      """  System time of the related PartTran record.  Pertains only to source from PartTran (TranSource = "P")  """  
      self.TranNum:int = obj["TranNum"]
      """  TranNum of the related PartTran record.  Pertains only to source from PartTran (TranSource = "P")  """  
      self.ARInvoiceNum:int = obj["ARInvoiceNum"]
      """  InvoiceNum of the related InvcHead record.  Pertains only to source from PartTran (TranSource = "I")  """  
      self.TransAmt:int = obj["TransAmt"]
      """  Transaction amount that this transaction posted to the related GlJrnDtl.  """  
      self.InvoiceLine:int = obj["InvoiceLine"]
      """  Invoice Line Number associated with this GL Journal  """  
      self.SeqNum:int = obj["SeqNum"]
      """  The sequence number associated with this GL journal  """  
      self.VendorNum:int = obj["VendorNum"]
      """  The Internal VendorNum that ties back to the Vendor master file.  This field is not directly maintainable.  """  
      self.APInvoiceNum:str = obj["APInvoiceNum"]
      """  Vendor's invoice number.  """  
      self.CreateDate:str = obj["CreateDate"]
      """  Date record was created  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  Fiscal year suffix.  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  The fiscal calendar year/suffix/period were derived from.  """  
      self.CreditAmount:int = obj["CreditAmount"]
      """  Credit Amount.  """  
      self.DebitAmount:int = obj["DebitAmount"]
      """  Debit Amount.  """  
      self.BookCreditAmount:int = obj["BookCreditAmount"]
      """  BookCreditAmount  """  
      self.BookDebitAmount:int = obj["BookDebitAmount"]
      """  Book Debit Amount  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  A unique code that identifies the document currency.  """  
      self.RecordType:str = obj["RecordType"]
      """   Indicates if this record contains account data only or reference data such as journal number, amounts, etc.  Valid  values are:
A - account data only
R - reference data  """  
      self.CorrAccUID:int = obj["CorrAccUID"]
      """  When a posting rule creates a pair of journal details balancing each other, each detail in the pair should reference the other one. This allows to show correspondence of accounts in reports. Support of reports that allow this being visible is not in the scope of this change.  """  
      self.ABTUID:str = obj["ABTUID"]
      """  this field equals ABTUID which was created during posting  """  
      self.RuleUID:int = obj["RuleUID"]
      """  Technical identifier.  """  
      self.Statistical:int = obj["Statistical"]
      """   Identifies if statistical information may be entered for the natural (chart) account.
Accounts can be used only for monetary amounts, both monetary and statistical amounts or only for statistical amounts.
0 = Only used for monetary amounts.
1 = Used for both monetary and statistical amounts.
2 = Only used for statistical amounts.  """  
      self.StatUOMCode:str = obj["StatUOMCode"]
      """  Statistical UOM code.  """  
      self.DebitStatAmt:int = obj["DebitStatAmt"]
      """  This field shows Debit statistical amount.  """  
      self.CreditStatAmt:int = obj["CreditStatAmt"]
      """  This field shows Credit statistical amount.  """  
      self.IsModifiedByUser:bool = obj["IsModifiedByUser"]
      """  IsModifiedByUser  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.MovementNum:int = obj["MovementNum"]
      """  MovementNum  """  
      self.MovementType:str = obj["MovementType"]
      """  MovementType  """  
      self.Plant:str = obj["Plant"]
      """  Plant  """  
      self.HeadNum:int = obj["HeadNum"]
      self.BitFlag:int = obj["BitFlag"]
      self.COADescription:str = obj["COADescription"]
      self.GLAccountGLAcctDisp:str = obj["GLAccountGLAcctDisp"]
      self.GLAccountAccountDesc:str = obj["GLAccountAccountDesc"]
      self.GLAccountGLShortAcct:str = obj["GLAccountGLShortAcct"]
      self.GLBookDescription:str = obj["GLBookDescription"]
      self.GLBookCurrencyCode:str = obj["GLBookCurrencyCode"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PRChkDedRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.HeadNum:int = obj["HeadNum"]
      """  Duplicated from related PRCheck.  """  
      self.DeductionID:str = obj["DeductionID"]
      """  The deduction Id that this check deduction record is related to.  """  
      self.DeductionNum:int = obj["DeductionNum"]
      """  DeductionNum of the related PREmpDed.  """  
      self.ScheduledAmt:int = obj["ScheduledAmt"]
      """  Deduction Amount scheduled to be taken.  Calculated based on the values stored in PREmpDed. This amount includes any CarryOverAmt.  """  
      self.ManualCalc:bool = obj["ManualCalc"]
      """  Indicates if the Deduction Amount is manually calculated.  The system will not calculate the DeductionAmount when ManualCalc = Yes.  """  
      self.CalcOrder:int = obj["CalcOrder"]
      """  An internally assigned integer which controls the order in which deductions are processed. It is created/used by the payroll calculation process. It is not the same thing as the PRDeduct.Priority ! Basically it is a sequential # which was generated by processing the deductions in priority order. An exception is for negative deductions, they are set to zero (highest priority). The CalcOrder comes into play when there are insufficient funds to take all the deductions. When this occurs the deductions are decreased in a descending CalcOrder sequence until the check becomes positive.  """  
      self.DeductionAmt:int = obj["DeductionAmt"]
      """  Deduction Amount taken. Normally this is the same a ScheduledAmt, except in the case where there was insufficient pay to take the deduction. In which case this value could be lower.  """  
      self.ClassID:str = obj["ClassID"]
      """  Payroll class ID that employee is currently assigned to.  A mirror image of PREmpMas. It is kept in sync by the PREmpMas write trigger.  """  
      self.Posted:bool = obj["Posted"]
      """  Mirror image of PRCheck.Posted.  """  
      self.EmpLink:str = obj["EmpLink"]
      """  Encoded value which identifies the employee. Mirror image of PRCheck.EmpLink.  """  
      self.CheckDate:str = obj["CheckDate"]
      """  mirror image of PRCheck.CheckDate  """  
      self.PriorDedYTD:int = obj["PriorDedYTD"]
      """  Deduction Year to date amount taken.  """  
      self.Voided:bool = obj["Voided"]
      """   An internal flag indicating if this is a Void payment transaction.
This is set by the P/R void check program.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.PrintHeadNum:int = obj["PrintHeadNum"]
      """  PrintHeadNum  """  
      self.EmpID:str = obj["EmpID"]
      self.FirstName:str = obj["FirstName"]
      """  First name of employee.  """  
      self.GroupID:str = obj["GroupID"]
      self.LastName:str = obj["LastName"]
      """  Last name of employee  """  
      self.Name:str = obj["Name"]
      """  This is the employees full name. This is not directly maintainable. It is a concatenation of the FirstName + MiddleInitial + LastName fields. It exists so that it can be used in browses or where ever the complete name in a first, middle, last fashion is required.  """  
      self.Reference:str = obj["Reference"]
      self.BitFlag:int = obj["BitFlag"]
      self.ClassIDDescription:str = obj["ClassIDDescription"]
      self.DeductionIDDescription:str = obj["DeductionIDDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PRChkDtlRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.HeadNum:int = obj["HeadNum"]
      """  Duplicated from the related PRCheck.  """  
      self.LineNum:int = obj["LineNum"]
      """  Integer assigned by the system which is used as one of the fields to uniquely identify the PRChkDtl record.  """  
      self.PayrollDate:str = obj["PayrollDate"]
      """  Date that the employee worked or earned the pay.  """  
      self.PayTypeID:str = obj["PayTypeID"]
      """   Identifies the Pay type of this payment record.  A foreign key to the PayType master table.  This must be a valid PayType where PayType.PremiumFactor <= 1.00.
Ex:( Regular, Holiday, Sick, Vacation . . .)  """  
      self.PayRate:int = obj["PayRate"]
      """  The employee's base hourly pay rate.  This rate does not include premium or shift differential factors.  It is defaulted from the PREmpMas.PayRate field.  """  
      self.BaseHours:int = obj["BaseHours"]
      """   Hours for non premium time.  Maintainable only if PayTypeID is not blank.
Stored as Hours.Hundreths. For example 3 1/2 hours is stored as 3.5  """  
      self.BasePay:int = obj["BasePay"]
      """  Base pay is the pay amount calculated non-premium hours employees base pay rate.  (see PremiumPay, ShiftPay).  It is calculated as  (BaseHours * PayRate) or set = to the employee salary amount.  It can be overridden in hours entry for salaried employees.  """  
      self.PremiumPayType:str = obj["PremiumPayType"]
      """  Identifies the premium Paytype of this payment record (Ex: OT, etc.).  A foreign key to the PayType master table.  This must be a valid PayType where PayType.PremiumFactor > 1.00.  """  
      self.PremiumHours:int = obj["PremiumHours"]
      """   Hours to be paid at the premium rate.  This is stored as Hours.Hundreths. For example 3 1/2 hours is stored as 3.5
This is disabled and zero if PremiumPaytype = blank.  """  
      self.PremiumBasePay:int = obj["PremiumBasePay"]
      """   The amount paid for premium hours not including the premium amount.  Not directly maintainable. (PremiumPayHours* Payrate )
Ex: rate = $10.00,  hours = 3, PremiumBasePay = 30.00. 
The Base Pay portion of the total premium pay amount  is kept separate from the Premium Pay portion for users who wish to track the premium portion of overtime expenses separately in general ledger.  """  
      self.PremiumPay:int = obj["PremiumPay"]
      """   Premium pay is the additional amount above the base pay that is being paid as a premium for this pay type. It is not directly maintainable.
For example PayHours = 8, PayRate = 10.00 and PremiumFactor = 1.5,  BasePay would be 80.00 and PremiumPay would be 40.00.
The Base Pay is kept separate from the Premium Pay for users who wish to track the premium portion of the pay separately in general ledger.
PremiumPayHours * (Payrate * (PremiumFactor - 1.00)).  """  
      self.Shift:int = obj["Shift"]
      """   Defaults from the EmpBasic.Shift when entered through payroll hours entry, or was from LaborHed.Shift is the case the record was created from labor transfer process.
Note:  When shift is changed in check entry the pay amounts may need to be recalculated if shift pay is active.  """  
      self.ShiftPay:int = obj["ShiftPay"]
      """   Shift pay is the amount paid due to shift differential.
(BaseHours * ShiftDifferential)  + 
PremiumHours * (ShiftDifferential * PremiumFactor).
PremiumFactor  is used only if PayType.IncludeShift = Yes. 
Note: Shift differential is either an additional percentage of payrate or an additional flat amount.  
For example PayHours = 8, PayRate = 10.00 and Shift differential is an extra 1.00 per hour. ShiftPay would be $8.00.
This is refreshed when changes are made to Shift, PayRate, or PayHours or PremiumHours or PayType.  """  
      self.ClassID:str = obj["ClassID"]
      """  Payroll class ID that employee is currently assigned to. A mirror image of PREmpMas. It is kept in sync by the PREmpMas write trigger.  """  
      self.Posted:bool = obj["Posted"]
      """  Mirror image of PRCheck.Posted.  """  
      self.EmpLink:str = obj["EmpLink"]
      """  Encoded value which identifies the employee. Mirror image of PRCheck.EmpLink.  """  
      self.CheckDate:str = obj["CheckDate"]
      """  mirror image of PRCheck.CheckDate.  This is not updated until the checks are posted.  """  
      self.FromLabor:bool = obj["FromLabor"]
      """  A internally used flag which indicates that this record was generated from a LaborHed record.  """  
      self.Voided:bool = obj["Voided"]
      """   An internal flag indicating if this is a Void payment transaction.
This is set by the P/R void check program.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.PrintHeadNum:int = obj["PrintHeadNum"]
      """  PrintHeadNum  """  
      self.IsOutdatedLabor:bool = obj["IsOutdatedLabor"]
      """  IsOutdatedLabor  """  
      self.DiffMethod:str = obj["DiffMethod"]
      self.DiffMethodDesc:str = obj["DiffMethodDesc"]
      self.DiffQualifier:str = obj["DiffQualifier"]
      self.DiffQualifierDesc:str = obj["DiffQualifierDesc"]
      self.DiffRate:int = obj["DiffRate"]
      self.EmpID:str = obj["EmpID"]
      self.FirstName:str = obj["FirstName"]
      """  First name of employee.  """  
      self.GroupID:str = obj["GroupID"]
      self.LastName:str = obj["LastName"]
      """  Last name of employee  """  
      self.Name:str = obj["Name"]
      """  This is the employees full name. This is not directly maintainable. It is a concatenation of the FirstName + MiddleInitial + LastName fields. It exists so that it can be used in browses or where ever the complete name in a first, middle, last fashion is required.  """  
      self.ShiftTimesDesc:str = obj["ShiftTimesDesc"]
      self.TotalHours:int = obj["TotalHours"]
      self.TotalPay:int = obj["TotalPay"]
      self.VoidedDate:str = obj["VoidedDate"]
      """  Used in VoidPRCheck - Date the check was voided.  """  
      self.AmountType:str = obj["AmountType"]
      self.DateRange:str = obj["DateRange"]
      """   DateRange specifies the range between record is created depending of payroll frequency, the possible values are:
"Outdated", labor processed before period begins
"In Pay Range", labor processed between perido begin and period ending
"Outrunning". labor processed after period ending  """  
      self.BitFlag:int = obj["BitFlag"]
      self.ClassIDDescription:str = obj["ClassIDDescription"]
      self.PayTypeIDDescription:str = obj["PayTypeIDDescription"]
      self.PremiumPayTypeIDDescription:str = obj["PremiumPayTypeIDDescription"]
      self.ShiftDescription:str = obj["ShiftDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PRChkTaxRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.HeadNum:int = obj["HeadNum"]
      """  Duplicated from related PRCheck.  """  
      self.TaxTblID:str = obj["TaxTblID"]
      """  Tax Table ID  """  
      self.TaxType:str = obj["TaxType"]
      """  Identifies the type of tax table.  Valid values are "FIT" - Federal, "SIT" - State, "FUTA" - Federal Unemployment, "SUTA" - State Unemployment,  "SS" - Social Security, "MED" - Medicare, "CITY" - Local, "CNTY" - County, "OTHR" - Other.  """  
      self.ClassID:str = obj["ClassID"]
      """  Payroll class ID that employee is currently assigned to. A mirror image of PREmpMas. It is kept in sync by the PREmpMas write trigger.  """  
      self.Posted:bool = obj["Posted"]
      """  Mirror image of PRCheck.Posted.  """  
      self.EmpLink:str = obj["EmpLink"]
      """  Encoded value which identifies the employee. Mirror image of PRCheck.EmpLink.  """  
      self.CheckDate:str = obj["CheckDate"]
      """  mirror image of PRCheck.CheckDate  """  
      self.TaxAmt:int = obj["TaxAmt"]
      """  Amount withheld on this check for a specific tax.  """  
      self.PriorTaxYTD:int = obj["PriorTaxYTD"]
      """  The Year to Date tax withheld  prior to this check. Current YTD is PriorTaxYTD + TaxAmt.  """  
      self.TaxableHours:int = obj["TaxableHours"]
      """  Taxable hours on this check for the tax jurisdiction.  This is the BaseHours and PremiumHours if the PayType is not exempt from the tax jurisdiction.  """  
      self.SupTaxableAmt:int = obj["SupTaxableAmt"]
      """  The taxable amount of supplemental pay for this check  for the tax jurisdiction.  """  
      self.SupTaxableHours:int = obj["SupTaxableHours"]
      """  The hours accumulated from supplemental pay records.  This is used in tax calc when tax basis is % of hours.  """  
      self.TaxableAmt:int = obj["TaxableAmt"]
      """  Pay check amount that is considered as taxable for this tax jurisdiction. This is calculated by the system as part of the payroll calculate routine.  """  
      self.PriorTaxableYTD:int = obj["PriorTaxableYTD"]
      """  The Year to Date taxable amount prior to this check. Current YTD is PriorTaxableYTD + TaxableAmt.  """  
      self.Active:bool = obj["Active"]
      """  Indicates if this tax record for the check is taxable as of the check date. Of course, if a tax was first taken it would have been taxable. This flag is used so that if after the check is posted it is discovered that it was taken in error the user can set this to NO which would reduce the year to date taxable amount from this date forward. This situation should not be a common occurrence; however it's more likely when employees' have multiple taxes that are deactivated/activated during the same year. It does not change the Tax withheld only taxable.  This flag is needed so that the "Recalculate" taxable amounts would work correctly.  """  
      self.ManualCalc:bool = obj["ManualCalc"]
      """  Indicates if the Tax Amount is manually calculated.  The system will not calculate the TaxAmount when ManualCalc = Yes.  """  
      self.Voided:bool = obj["Voided"]
      """   An internal flag indicating if this is a Void payment transaction.
This is set by the P/R void check program.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.PrintHeadNum:int = obj["PrintHeadNum"]
      """  PrintHeadNum  """  
      self.CreditAmount:int = obj["CreditAmount"]
      self.EmpID:str = obj["EmpID"]
      self.FilingStatus:str = obj["FilingStatus"]
      self.FirstName:str = obj["FirstName"]
      """  First name of employee.  """  
      self.GroupID:str = obj["GroupID"]
      self.LastName:str = obj["LastName"]
      """  Last name of employee  """  
      self.Name:str = obj["Name"]
      """  This is the employees full name. This is not directly maintainable. It is a concatenation of the FirstName + MiddleInitial + LastName fields. It exists so that it can be used in browses or where ever the complete name in a first, middle, last fashion is required.  """  
      self.TaxDesc:str = obj["TaxDesc"]
      self.BitFlag:int = obj["BitFlag"]
      self.ClassIDDescription:str = obj["ClassIDDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PayrollCheckEntryTableset:
   def __init__(self, obj):
      self.PRCheck:list[Erp_Tablesets_PRCheckRow] = obj["PRCheck"]
      self.PRChkDed:list[Erp_Tablesets_PRChkDedRow] = obj["PRChkDed"]
      self.PRChkDtl:list[Erp_Tablesets_PRChkDtlRow] = obj["PRChkDtl"]
      self.PRChkTax:list[Erp_Tablesets_PRChkTaxRow] = obj["PRChkTax"]
      self.PRCheckTGLC:list[Erp_Tablesets_PRCheckTGLCRow] = obj["PRCheckTGLC"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_UpdExtPayrollCheckEntryTableset:
   def __init__(self, obj):
      self.PRCheck:list[Erp_Tablesets_PRCheckRow] = obj["PRCheck"]
      self.PRChkDed:list[Erp_Tablesets_PRChkDedRow] = obj["PRChkDed"]
      self.PRChkDtl:list[Erp_Tablesets_PRChkDtlRow] = obj["PRChkDtl"]
      self.PRChkTax:list[Erp_Tablesets_PRChkTaxRow] = obj["PRChkTax"]
      self.PRCheckTGLC:list[Erp_Tablesets_PRCheckTGLCRow] = obj["PRCheckTGLC"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GeneratePayChecksVerification_input:
   """ Required : 
   groupID
   """  
   def __init__(self, obj):
      self.groupID:str = obj["groupID"]
      """  The group id to get the configuration options  """  
      pass

class GeneratePayChecksVerification_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.VerificationMsg:str = obj["parameters"]
      pass

      """  output parameters  """  

class GeneratePayChecks_input:
   """ Required : 
   GroupID
   HeadNum
   ds
   """  
   def __init__(self, obj):
      self.GroupID:str = obj["GroupID"]
      """  The group id to generate paychecks for  """  
      self.HeadNum:int = obj["HeadNum"]
      """  The current PRCheck.HeadNum record.  Is used to
            rebuild the dataset so the data is current. Not required.  If the value
            is 0, a refreshed dataset won't be passed back.  """  
      self.ds:list[Erp_Tablesets_PayrollCheckEntryTableset] = obj["ds"]
      pass

class GeneratePayChecks_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PayrollCheckEntryTableset] = obj["ds"]
      self.OutNoCheckMessage:str = obj["parameters"]
      self.OutNotApprovedLaborMessage:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetByID_input:
   """ Required : 
   headNum
   """  
   def __init__(self, obj):
      self.headNum:int = obj["headNum"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_PayrollCheckEntryTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_PayrollCheckEntryTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_PayrollCheckEntryTableset] = obj["returnObj"]
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

class GetGLEntries_input:
   """ Required : 
   EmpID
   CheckNum
   """  
   def __init__(self, obj):
      self.EmpID:str = obj["EmpID"]
      """  Employee ID  """  
      self.CheckNum:int = obj["CheckNum"]
      """  Check Number  """  
      pass

class GetGLEntries_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_PayrollCheckEntryTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_PRCheckListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewPRCheckForGroup_input:
   """ Required : 
   GroupID
   ds
   """  
   def __init__(self, obj):
      self.GroupID:str = obj["GroupID"]
      """  The group id to add the payroll check to  """  
      self.ds:list[Erp_Tablesets_PayrollCheckEntryTableset] = obj["ds"]
      pass

class GetNewPRCheckForGroup_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PayrollCheckEntryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewPRCheckTGLC_input:
   """ Required : 
   ds
   headNum
   tgLCTranNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PayrollCheckEntryTableset] = obj["ds"]
      self.headNum:int = obj["headNum"]
      self.tgLCTranNum:int = obj["tgLCTranNum"]
      pass

class GetNewPRCheckTGLC_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PayrollCheckEntryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewPRCheck_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PayrollCheckEntryTableset] = obj["ds"]
      pass

class GetNewPRCheck_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PayrollCheckEntryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewPRChkDed_input:
   """ Required : 
   ds
   headNum
   deductionID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PayrollCheckEntryTableset] = obj["ds"]
      self.headNum:int = obj["headNum"]
      self.deductionID:str = obj["deductionID"]
      pass

class GetNewPRChkDed_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PayrollCheckEntryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewPRChkDtl_input:
   """ Required : 
   ds
   headNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PayrollCheckEntryTableset] = obj["ds"]
      self.headNum:int = obj["headNum"]
      pass

class GetNewPRChkDtl_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PayrollCheckEntryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewPRChkTax_input:
   """ Required : 
   ds
   headNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PayrollCheckEntryTableset] = obj["ds"]
      self.headNum:int = obj["headNum"]
      pass

class GetNewPRChkTax_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PayrollCheckEntryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRowsByEmpID_input:
   """ Required : 
   empID
   whereClausePRCheck
   whereClausePRChkDtl
   whereClausePRChkDed
   whereClausePRChkTax
   whereClausePRCheckTGLC
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.empID:str = obj["empID"]
      """  Employee ID  """  
      self.whereClausePRCheck:str = obj["whereClausePRCheck"]
      """  WhereClause Payroll Check  """  
      self.whereClausePRChkDtl:str = obj["whereClausePRChkDtl"]
      """  WhereClause Payroll Check Details  """  
      self.whereClausePRChkDed:str = obj["whereClausePRChkDed"]
      """  WhereClause Payroll Check Deductions  """  
      self.whereClausePRChkTax:str = obj["whereClausePRChkTax"]
      """  WhereClause Payroll Check Tax  """  
      self.whereClausePRCheckTGLC:str = obj["whereClausePRCheckTGLC"]
      """  WhereClause Payroll Check TranGLC  """  
      self.pageSize:int = obj["pageSize"]
      """  PageSize  """  
      self.absolutePage:int = obj["absolutePage"]
      """  Absolute Page  """  
      pass

class GetRowsByEmpID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_PayrollCheckEntryTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetRowsFromAutoBankRec_input:
   """ Required : 
   ipHeadNum
   ipWhereClausePRCheck
   ipWhereClausePRChkDtl
   ipWhereClausePRChkDed
   ipWhereClausePRChkTax
   ipWhereClausePRCheckTGLC
   ipPageSize
   ipAbsolutePage
   """  
   def __init__(self, obj):
      self.ipHeadNum:str = obj["ipHeadNum"]
      """  Head No  """  
      self.ipWhereClausePRCheck:str = obj["ipWhereClausePRCheck"]
      """  WhereClause Payroll Check  """  
      self.ipWhereClausePRChkDtl:str = obj["ipWhereClausePRChkDtl"]
      """  WhereClause Payroll Check Details  """  
      self.ipWhereClausePRChkDed:str = obj["ipWhereClausePRChkDed"]
      """  WhereClause Payroll Check Deductions  """  
      self.ipWhereClausePRChkTax:str = obj["ipWhereClausePRChkTax"]
      """  WhereClause Payroll Check Tax  """  
      self.ipWhereClausePRCheckTGLC:str = obj["ipWhereClausePRCheckTGLC"]
      """  WhereClause Payroll Check TranGLC  """  
      self.ipPageSize:int = obj["ipPageSize"]
      """  PageSize  """  
      self.ipAbsolutePage:int = obj["ipAbsolutePage"]
      """  Absolute Page  """  
      pass

class GetRowsFromAutoBankRec_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_PayrollCheckEntryTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.opMorePages:bool = obj["opMorePages"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClausePRCheck
   whereClausePRChkDed
   whereClausePRChkDtl
   whereClausePRChkTax
   whereClausePRCheckTGLC
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClausePRCheck:str = obj["whereClausePRCheck"]
      self.whereClausePRChkDed:str = obj["whereClausePRChkDed"]
      self.whereClausePRChkDtl:str = obj["whereClausePRChkDtl"]
      self.whereClausePRChkTax:str = obj["whereClausePRChkTax"]
      self.whereClausePRCheckTGLC:str = obj["whereClausePRCheckTGLC"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_PayrollCheckEntryTableset] = obj["returnObj"]
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

class RecalcPayRate_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PayrollCheckEntryTableset] = obj["ds"]
      pass

class RecalcPayRate_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PayrollCheckEntryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtPayrollCheckEntryTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtPayrollCheckEntryTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class UpdatePRChkDed_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PayrollCheckEntryTableset] = obj["ds"]
      pass

class UpdatePRChkDed_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PayrollCheckEntryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class UpdatePRChkTax_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PayrollCheckEntryTableset] = obj["ds"]
      pass

class UpdatePRChkTax_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PayrollCheckEntryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PayrollCheckEntryTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PayrollCheckEntryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class getClientFileName_input:
   """ Required : 
   IP_ServerFileName
   """  
   def __init__(self, obj):
      self.IP_ServerFileName:str = obj["IP_ServerFileName"]
      pass

class getClientFileName_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

