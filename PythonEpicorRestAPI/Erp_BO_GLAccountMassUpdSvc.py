import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.GLAccountMassUpdSvc
# Description: General Ledger Accounts Massive Update Service
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GLAccountMassUpdSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GLAccountMassUpdSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_GLAccountMassUpds(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get GLAccountMassUpds items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_GLAccountMassUpds
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.COARow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GLAccountMassUpdSvc/GLAccountMassUpds",headers=creds) as resp:
           return await resp.json()

async def post_GLAccountMassUpds(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_GLAccountMassUpds
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.COARow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.COARow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLAccountMassUpdSvc/GLAccountMassUpds", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_GLAccountMassUpds_Company_COACode(Company, COACode, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the GLAccountMassUpd item
   Description: Calls GetByID to retrieve the GLAccountMassUpd item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_GLAccountMassUpd
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param COACode: Desc: COACode   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.COARow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GLAccountMassUpdSvc/GLAccountMassUpds(" + Company + "," + COACode + ")",headers=creds) as resp:
           return await resp.json()

async def patch_GLAccountMassUpds_Company_COACode(Company, COACode, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update GLAccountMassUpd for the service
   Description: Calls UpdateExt to update GLAccountMassUpd. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_GLAccountMassUpd
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param COACode: Desc: COACode   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.COARow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.GLAccountMassUpdSvc/GLAccountMassUpds(" + Company + "," + COACode + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_GLAccountMassUpds_Company_COACode(Company, COACode, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete GLAccountMassUpd item
   Description: Call UpdateExt to delete GLAccountMassUpd item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_GLAccountMassUpd
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param COACode: Desc: COACode   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.GLAccountMassUpdSvc/GLAccountMassUpds(" + Company + "," + COACode + ")",headers=creds) as resp:
           return await resp.json()

async def get_SegAccts(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get SegAccts items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_SegAccts
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.SegAcctRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GLAccountMassUpdSvc/SegAccts",headers=creds) as resp:
           return await resp.json()

async def post_SegAccts(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_SegAccts
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.SegAcctRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.SegAcctRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLAccountMassUpdSvc/SegAccts", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_SegAccts_Company_COACode_CurrencyCode(Company, COACode, CurrencyCode, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the SegAcct item
   Description: Calls GetByID to retrieve the SegAcct item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_SegAcct
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param COACode: Desc: COACode   Required: True   Allow empty value : True
      :param CurrencyCode: Desc: CurrencyCode   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.SegAcctRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GLAccountMassUpdSvc/SegAccts(" + Company + "," + COACode + "," + CurrencyCode + ")",headers=creds) as resp:
           return await resp.json()

async def patch_SegAccts_Company_COACode_CurrencyCode(Company, COACode, CurrencyCode, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update SegAcct for the service
   Description: Calls UpdateExt to update SegAcct. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_SegAcct
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param COACode: Desc: COACode   Required: True   Allow empty value : True
      :param CurrencyCode: Desc: CurrencyCode   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.SegAcctRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.GLAccountMassUpdSvc/SegAccts(" + Company + "," + COACode + "," + CurrencyCode + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_SegAccts_Company_COACode_CurrencyCode(Company, COACode, CurrencyCode, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete SegAcct item
   Description: Call UpdateExt to delete SegAcct item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_SegAcct
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param COACode: Desc: COACode   Required: True   Allow empty value : True
      :param CurrencyCode: Desc: CurrencyCode   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.GLAccountMassUpdSvc/SegAccts(" + Company + "," + COACode + "," + CurrencyCode + ")",headers=creds) as resp:
           return await resp.json()

async def get_SegOpts(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get SegOpts items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_SegOpts
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.SegOptRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GLAccountMassUpdSvc/SegOpts",headers=creds) as resp:
           return await resp.json()

async def post_SegOpts(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_SegOpts
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.SegOptRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.SegOptRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLAccountMassUpdSvc/SegOpts", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_SegOpts_SysRowID(SysRowID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the SegOpt item
   Description: Calls GetByID to retrieve the SegOpt item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_SegOpt
      :param SysRowID: Desc: SysRowID   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.SegOptRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GLAccountMassUpdSvc/SegOpts(" + SysRowID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_SegOpts_SysRowID(SysRowID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update SegOpt for the service
   Description: Calls UpdateExt to update SegOpt. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_SegOpt
      :param SysRowID: Desc: SysRowID   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.SegOptRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.GLAccountMassUpdSvc/SegOpts(" + SysRowID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_SegOpts_SysRowID(SysRowID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete SegOpt item
   Description: Call UpdateExt to delete SegOpt item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_SegOpt
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.GLAccountMassUpdSvc/SegOpts(" + SysRowID + ")",headers=creds) as resp:
           return await resp.json()

async def get_SegRanges(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get SegRanges items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_SegRanges
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.SegRangeRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GLAccountMassUpdSvc/SegRanges",headers=creds) as resp:
           return await resp.json()

async def post_SegRanges(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_SegRanges
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.SegRangeRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.SegRangeRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLAccountMassUpdSvc/SegRanges", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_SegRanges_SysRowID(SysRowID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the SegRange item
   Description: Calls GetByID to retrieve the SegRange item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_SegRange
      :param SysRowID: Desc: SysRowID   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.SegRangeRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GLAccountMassUpdSvc/SegRanges(" + SysRowID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_SegRanges_SysRowID(SysRowID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update SegRange for the service
   Description: Calls UpdateExt to update SegRange. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_SegRange
      :param SysRowID: Desc: SysRowID   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.SegRangeRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.GLAccountMassUpdSvc/SegRanges(" + SysRowID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_SegRanges_SysRowID(SysRowID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete SegRange item
   Description: Call UpdateExt to delete SegRange item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_SegRange
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.GLAccountMassUpdSvc/SegRanges(" + SysRowID + ")",headers=creds) as resp:
           return await resp.json()

async def get_SegRes(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get SegRes items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_SegRes
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.SegResRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GLAccountMassUpdSvc/SegRes",headers=creds) as resp:
           return await resp.json()

async def post_SegRes(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_SegRes
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.SegResRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.SegResRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLAccountMassUpdSvc/SegRes", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_SegRes_SysRowID(SysRowID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the SegRe item
   Description: Calls GetByID to retrieve the SegRe item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_SegRe
      :param SysRowID: Desc: SysRowID   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.SegResRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GLAccountMassUpdSvc/SegRes(" + SysRowID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_SegRes_SysRowID(SysRowID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update SegRe for the service
   Description: Calls UpdateExt to update SegRe. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_SegRe
      :param SysRowID: Desc: SysRowID   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.SegResRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.GLAccountMassUpdSvc/SegRes(" + SysRowID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_SegRes_SysRowID(SysRowID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete SegRe item
   Description: Call UpdateExt to delete SegRe item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_SegRe
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.GLAccountMassUpdSvc/SegRes(" + SysRowID + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.COAListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GLAccountMassUpdSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseCOA, whereClauseSegAcct, whereClauseSegOpt, whereClauseSegRange, whereClauseSegRes, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClauseCOA=" + whereClauseCOA
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseSegAcct=" + whereClauseSegAcct
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseSegOpt=" + whereClauseSegOpt
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseSegRange=" + whereClauseSegRange
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseSegRes=" + whereClauseSegRes
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GLAccountMassUpdSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(coACode, epicorHeaders = None):
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
   params += "coACode=" + coACode

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GLAccountMassUpdSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GLAccountMassUpdSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_ChangeCurrencyAccount(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeCurrencyAccount
   Description: Change currency account and load currencies data according selection.
   OperationID: ChangeCurrencyAccount
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeCurrencyAccount_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeCurrencyAccount_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLAccountMassUpdSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DeleteCurrencyAccount(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DeleteCurrencyAccount
   Description: Delete currency account.
   OperationID: DeleteCurrencyAccount
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DeleteCurrencyAccount_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteCurrencyAccount_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLAccountMassUpdSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeAllowed(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeAllowed
   Description: Change Currency Allowed
   OperationID: ChangeAllowed
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeAllowed_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeAllowed_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLAccountMassUpdSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeRevalue(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeRevalue
   Description: Change Revalue Option
   OperationID: ChangeRevalue
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeRevalue_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeRevalue_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLAccountMassUpdSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewSegRange(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewSegRange
   Description: Add a row to datatable SegRange
   OperationID: GetNewSegRange
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewSegRange_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewSegRange_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLAccountMassUpdSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewSegOpt(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewSegOpt
   Description: Add a row to datatable SegOpt
   OperationID: GetNewSegOpt
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewSegOpt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewSegOpt_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLAccountMassUpdSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewSegRes(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewSegRes
   Description: Add a row to datatable SegRes
   OperationID: GetNewSegRes
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewSegRes_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewSegRes_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLAccountMassUpdSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetListsForProcess(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetListsForProcess
   Description: Builds list for ranges, options, restrictions, and currency accounts for the Natural Account Mass Update process
   OperationID: GetListsForProcess
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetListsForProcess_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetListsForProcess_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLAccountMassUpdSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetCOACategoriesFromList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetCOACategoriesFromList
   Description: Create Natural Account COA Categories datatable for selection
   OperationID: GetCOACategoriesFromList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetCOACategoriesFromList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCOACategoriesFromList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLAccountMassUpdSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DefaultsOnAddSegAcct(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DefaultsOnAddSegAcct
   Description: Check if account is valid and set description for it
   OperationID: DefaultsOnAddSegAcct
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DefaultsOnAddSegAcct_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DefaultsOnAddSegAcct_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLAccountMassUpdSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewCOA(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewCOA
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewCOA
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewCOA_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewCOA_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLAccountMassUpdSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLAccountMassUpdSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GLAccountMassUpdSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GLAccountMassUpdSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLAccountMassUpdSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLAccountMassUpdSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_COAListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_COAListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_COARow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_COARow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_SegAcctRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_SegAcctRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_SegOptRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_SegOptRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_SegRangeRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_SegRangeRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_SegResRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_SegResRow] = obj["value"]
      pass

class Erp_Tablesets_COAListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.COACode:str = obj["COACode"]
      """  Chart of Account ID  """  
      self.Description:str = obj["Description"]
      """  The description or Name of this Chart of Accounts.  """  
      self.SeparatorChar:str = obj["SeparatorChar"]
      """  This is the character that is displayed between each segment of the GL Accounts.  Tilde (~~), Tick (`) and Vertical Bar (|) are invalid separators.  """  
      self.PerBalFmt:str = obj["PerBalFmt"]
      """  Internally used field.  Not intended for end-user use.  Tilde delimited string indicating the segments used in the period balance account.  Example: 1~2~5 indicates segments 1, 2 and 5 are used to construct the balance account number.  """  
      self.TBBalFmt:str = obj["TBBalFmt"]
      """  Internally used field.  Not intended for end-user use.  Tilde delimited string indicating the segments used in the trial balance account. Example: 1~3~4 indicates segments 1, 3 and 4 are used to construct the balance account number.  """  
      self.FmtChgDate:str = obj["FmtChgDate"]
      """  Internal field used by the GL Account Control to identify when cache needs to be updated with the new COA structure.  This is updated by the COASegment write and delete triggers.  It is not intended for end user use.  Only changes important to the GL Account control updates this field's value.  """  
      self.FmtChgTime:int = obj["FmtChgTime"]
      """  Internal field used by the GL Account Control to identify when cache needs to be updated with the new COA structure.  This is updated by the COASegment write and delete triggers.  It is not intended for end user use.  Only changes important to the GL Account control updates this field's value.  """  
      self.CtrlSegList:str = obj["CtrlSegList"]
      """  Internally used field.  Not intended for end-user use.  Tilde delimited string indicating the controlled segments.  Example: 1~2~5 indicates segments 1, 2 and 5 are controlled.  This field is to be used in those situations where reading all of the COASegements via the Dynamic index is too much overhead.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.GlobalCOA:bool = obj["GlobalCOA"]
      """  Marks the COA as Global  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Disables this record from receiving global updates  """  
      self.RebuildGLAccts:bool = obj["RebuildGLAccts"]
      """  Internal logical used by UI that indicates if GLAccounts exist for this COA and that the display gl account must be rebuilt  """  
      self.ChartInUse:bool = obj["ChartInUse"]
      """  Logical indicating if the chart has been used  """  
      self.ChartLength:int = obj["ChartLength"]
      """  Sum of the COASegment.MaxLength entries.  """  
      self.MasterCOA:bool = obj["MasterCOA"]
      """  Logical indicating if this COA is the Master COA.  """  
      self.NbrSegments:int = obj["NbrSegments"]
      """  Total number of segments defined for this COA  """  
      self.HasRefSegment:bool = obj["HasRefSegment"]
      """  logical indicating if this chart has a segment defined as use ref entity where the reference entity = GLCOARefType  """  
      self.ConsInUse:bool = obj["ConsInUse"]
      """  Logical indicating if this chart of accounts is subject to consolidation  """  
      self.RebuildBalances:bool = obj["RebuildBalances"]
      """  Logical indicating the balances are to be rebuilt due to a change in balance structure  """  
      self.CreateDefCat:bool = obj["CreateDefCat"]
      """  Logical indicating if default categories are to be created  """  
      self.GlbFlag:bool = obj["GlbFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_COARow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.COACode:str = obj["COACode"]
      """  Chart of Account ID  """  
      self.Description:str = obj["Description"]
      """  The description or Name of this Chart of Accounts.  """  
      self.SeparatorChar:str = obj["SeparatorChar"]
      """  This is the character that is displayed between each segment of the GL Accounts.  Tilde (~~), Tick (`) and Vertical Bar (|) are invalid separators.  """  
      self.PerBalFmt:str = obj["PerBalFmt"]
      """  Internally used field.  Not intended for end-user use.  Tilde delimited string indicating the segments used in the period balance account.  Example: 1~2~5 indicates segments 1, 2 and 5 are used to construct the balance account number.  """  
      self.TBBalFmt:str = obj["TBBalFmt"]
      """  Internally used field.  Not intended for end-user use.  Tilde delimited string indicating the segments used in the trial balance account. Example: 1~3~4 indicates segments 1, 3 and 4 are used to construct the balance account number.  """  
      self.FmtChgDate:str = obj["FmtChgDate"]
      """  Internal field used by the GL Account Control to identify when cache needs to be updated with the new COA structure.  This is updated by the COASegment write and delete triggers.  It is not intended for end user use.  Only changes important to the GL Account control updates this field's value.  """  
      self.FmtChgTime:int = obj["FmtChgTime"]
      """  Internal field used by the GL Account Control to identify when cache needs to be updated with the new COA structure.  This is updated by the COASegment write and delete triggers.  It is not intended for end user use.  Only changes important to the GL Account control updates this field's value.  """  
      self.CtrlSegList:str = obj["CtrlSegList"]
      """  Internally used field.  Not intended for end-user use.  Tilde delimited string indicating the controlled segments.  Example: 1~2~5 indicates segments 1, 2 and 5 are controlled.  This field is to be used in those situations where reading all of the COASegements via the Dynamic index is too much overhead.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.GlobalCOA:bool = obj["GlobalCOA"]
      """  Marks the COA as Global  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Disables this record from receiving global updates  """  
      self.RebuildGLAccts:bool = obj["RebuildGLAccts"]
      """  Internal logical used by UI that indicates if GLAccounts exist for this COA and that the display gl account must be rebuilt  """  
      self.PESunatCOA:str = obj["PESunatCOA"]
      """  Peru CSF: SUNAT Chart of Accounts Code  """  
      self.ChartInUse:bool = obj["ChartInUse"]
      """  Logical indicating if the chart has been used  """  
      self.CreateDefCat:bool = obj["CreateDefCat"]
      """  Logical indicating if default categories are to be created  """  
      self.EnableGlobalCOA:bool = obj["EnableGlobalCOA"]
      self.EnableGlobalLock:bool = obj["EnableGlobalLock"]
      self.GlbFlag:bool = obj["GlbFlag"]
      self.HasRefSegment:bool = obj["HasRefSegment"]
      """  logical indicating if this chart has a segment defined as use ref entity where the reference entity = GLCOARefType  """  
      self.MasterCOA:bool = obj["MasterCOA"]
      """  Logical indicating if this COA is the Master COA.  """  
      self.NbrSegments:int = obj["NbrSegments"]
      """  Total number of segments defined for this COA  """  
      self.RebuildBalances:bool = obj["RebuildBalances"]
      """  Logical indicating the balances are to be rebuilt due to a change in balance structure  """  
      self.ChartLength:int = obj["ChartLength"]
      """  Sum of the COASegment.MaxLength entries.  """  
      self.ConsInUse:bool = obj["ConsInUse"]
      """  Logical indicating if this chart of accounts is subject to consolidation  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_SegAcctRow:
   def __init__(self, obj):
      self.AccrualAccount:str = obj["AccrualAccount"]
      """  The natural account used as the accrual account.  """  
      self.AccrualGLDesc:str = obj["AccrualGLDesc"]
      """  Accrual GL Account description  """  
      self.AccrualSegVal1:str = obj["AccrualSegVal1"]
      """  AccrualSegVal1  """  
      self.AccrualSegVal10:str = obj["AccrualSegVal10"]
      """  AccrualSegVal10  """  
      self.AccrualSegVal11:str = obj["AccrualSegVal11"]
      """  AccrualSegVal11  """  
      self.AccrualSegVal12:str = obj["AccrualSegVal12"]
      """  AccrualSegVal12  """  
      self.AccrualSegVal13:str = obj["AccrualSegVal13"]
      """  AccrualSegVal13  """  
      self.AccrualSegVal14:str = obj["AccrualSegVal14"]
      """  AccrualSegVal14  """  
      self.AccrualSegVal15:str = obj["AccrualSegVal15"]
      """  AccrualSegVal15  """  
      self.AccrualSegVal16:str = obj["AccrualSegVal16"]
      """  AccrualSegVal16  """  
      self.AccrualSegVal17:str = obj["AccrualSegVal17"]
      """  AccrualSegVal17  """  
      self.AccrualSegVal18:str = obj["AccrualSegVal18"]
      """  AccrualSegVal18  """  
      self.AccrualSegVal19:str = obj["AccrualSegVal19"]
      """  AccrualSegVal19  """  
      self.AccrualSegVal2:str = obj["AccrualSegVal2"]
      """  AccrualSegVal2  """  
      self.AccrualSegVal20:str = obj["AccrualSegVal20"]
      """  AccrualSegVal20  """  
      self.AccrualSegVal3:str = obj["AccrualSegVal3"]
      """  AccrualSegVal3  """  
      self.AccrualSegVal4:str = obj["AccrualSegVal4"]
      """  AccrualSegVal4  """  
      self.AccrualSegVal5:str = obj["AccrualSegVal5"]
      """  AccrualSegVal5  """  
      self.AccrualSegVal6:str = obj["AccrualSegVal6"]
      """  AccrualSegVal6  """  
      self.AccrualSegVal7:str = obj["AccrualSegVal7"]
      """  AccrualSegVal7  """  
      self.AccrualSegVal8:str = obj["AccrualSegVal8"]
      """  AccrualSegVal8  """  
      self.AccrualSegVal9:str = obj["AccrualSegVal9"]
      """  AccrualSegVal9  """  
      self.Allowed:bool = obj["Allowed"]
      """  Indicates the currency can be used as a transactional currency.  """  
      self.COACode:str = obj["COACode"]
      """  Chart of Account ID  """  
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.CurrDesc:str = obj["CurrDesc"]
      """  Description of the currency  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  Unique code identifying the currency.  Only those values defined in the CurrencyMaster are allowed.  """  
      self.CurrencyID:str = obj["CurrencyID"]
      """  This is the updatable version of CurrencyCode.  This currency cannot be a record already in the currency table.  """  
      self.CurrName:str = obj["CurrName"]
      """   Used to print as the suffix to the word amount line printed on checks.  For example:
One Hundred and 00/100 Dollars. In this case  "Dollars" is the CurrName  """  
      self.CurrSymbol:str = obj["CurrSymbol"]
      """  A symbol that identifies the currency. Used on Forms and displays  """  
      self.DocumentDesc:str = obj["DocumentDesc"]
      """   An extended description that can be used on documents such as
POs and invoices.  """  
      self.GainAccount:str = obj["GainAccount"]
      """  The natural account used for booking currency gains.  """  
      self.GainGLDesc:str = obj["GainGLDesc"]
      """  Gain GL Account Description  """  
      self.GainSegVal1:str = obj["GainSegVal1"]
      """  GainSegVal1  """  
      self.GainSegVal10:str = obj["GainSegVal10"]
      """  GainSegVal10  """  
      self.GainSegVal11:str = obj["GainSegVal11"]
      """  GainSegVal11  """  
      self.GainSegVal12:str = obj["GainSegVal12"]
      """  GainSegVal12  """  
      self.GainSegVal13:str = obj["GainSegVal13"]
      """  GainSegVal13  """  
      self.GainSegVal14:str = obj["GainSegVal14"]
      """  GainSegVal14  """  
      self.GainSegVal15:str = obj["GainSegVal15"]
      """  GainSegVal15  """  
      self.GainSegVal16:str = obj["GainSegVal16"]
      """  GainSegVal16  """  
      self.GainSegVal17:str = obj["GainSegVal17"]
      """  GainSegVal17  """  
      self.GainSegVal18:str = obj["GainSegVal18"]
      """  GainSegVal18  """  
      self.GainSegVal19:str = obj["GainSegVal19"]
      """  GainSegVal19  """  
      self.GainSegVal2:str = obj["GainSegVal2"]
      """  GainSegVal2  """  
      self.GainSegVal20:str = obj["GainSegVal20"]
      """  GainSegVal20  """  
      self.GainSegVal3:str = obj["GainSegVal3"]
      """  GainSegVal3  """  
      self.GainSegVal4:str = obj["GainSegVal4"]
      """  GainSegVal4  """  
      self.GainSegVal5:str = obj["GainSegVal5"]
      """  GainSegVal5  """  
      self.GainSegVal6:str = obj["GainSegVal6"]
      """  GainSegVal6  """  
      self.GainSegVal7:str = obj["GainSegVal7"]
      """  GainSegVal7  """  
      self.GainSegVal8:str = obj["GainSegVal8"]
      """  GainSegVal8  """  
      self.GainSegVal9:str = obj["GainSegVal9"]
      """  GainSegVal9  """  
      self.LossAccount:str = obj["LossAccount"]
      """  The natural account used for booking currency losses.  """  
      self.LossGLDesc:str = obj["LossGLDesc"]
      """  Loss GL Account Description  """  
      self.LossSegVal1:str = obj["LossSegVal1"]
      """  LossSegVal1  """  
      self.LossSegVal10:str = obj["LossSegVal10"]
      """  LossSegVal10  """  
      self.LossSegVal11:str = obj["LossSegVal11"]
      """  LossSegVal11  """  
      self.LossSegVal12:str = obj["LossSegVal12"]
      """  LossSegVal12  """  
      self.LossSegVal13:str = obj["LossSegVal13"]
      """  LossSegVal13  """  
      self.LossSegVal14:str = obj["LossSegVal14"]
      """  LossSegVal14  """  
      self.LossSegVal15:str = obj["LossSegVal15"]
      """  LossSegVal15  """  
      self.LossSegVal16:str = obj["LossSegVal16"]
      """  LossSegVal16  """  
      self.LossSegVal17:str = obj["LossSegVal17"]
      """  LossSegVal17  """  
      self.LossSegVal18:str = obj["LossSegVal18"]
      """  LossSegVal18  """  
      self.LossSegVal19:str = obj["LossSegVal19"]
      """  LossSegVal19  """  
      self.LossSegVal2:str = obj["LossSegVal2"]
      """  LossSegVal2  """  
      self.LossSegVal20:str = obj["LossSegVal20"]
      """  LossSegVal20  """  
      self.LossSegVal3:str = obj["LossSegVal3"]
      """  LossSegVal3  """  
      self.LossSegVal4:str = obj["LossSegVal4"]
      """  LossSegVal4  """  
      self.LossSegVal5:str = obj["LossSegVal5"]
      """  LossSegVal5  """  
      self.LossSegVal6:str = obj["LossSegVal6"]
      """  LossSegVal6  """  
      self.LossSegVal7:str = obj["LossSegVal7"]
      """  LossSegVal7  """  
      self.LossSegVal8:str = obj["LossSegVal8"]
      """  LossSegVal8  """  
      self.LossSegVal9:str = obj["LossSegVal9"]
      """  LossSegVal9  """  
      self.Revalue:int = obj["Revalue"]
      """   Indicates if the transaction currency amount can be revalued.  Valid values are:
0 - no revalulation (deafult)
1 - only profits
2 - only losses
3 - both profit and losses  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_SegOptRow:
   def __init__(self, obj):
      self.COACode:str = obj["COACode"]
      """  Chart of Account ID  """  
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.DefaultSegment:str = obj["DefaultSegment"]
      """  Indicates the default segment value to be used for this natural account.  """  
      self.SegmentCode:str = obj["SegmentCode"]
      """  Segment value used to construct the GL Account.  """  
      self.ValOption:str = obj["ValOption"]
      """   Indicates if a segment is used for the natural account.  Valid values are:
M - Mandatory
O - Optional
N - Not Used  """  
      self.SegmentName:str = obj["SegmentName"]
      self.SegmentNbr:int = obj["SegmentNbr"]
      self.SubSegmentNbr:int = obj["SubSegmentNbr"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_SegRangeRow:
   def __init__(self, obj):
      self.COACode:str = obj["COACode"]
      """  Chart of Account ID  """  
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.EndVal:str = obj["EndVal"]
      self.RangeID:str = obj["RangeID"]
      """  From code to code  """  
      self.SegmentNbr:int = obj["SegmentNbr"]
      self.StartVal:str = obj["StartVal"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_SegResRow:
   def __init__(self, obj):
      self.COACode:str = obj["COACode"]
      """  Chart of Account ID  """  
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.FctBlocked:bool = obj["FctBlocked"]
      """  Indicates if GL Account entry is prohibited  """  
      self.RestrictID:str = obj["RestrictID"]
      """  Application DLL name  """  
      self.SegmentCode:str = obj["SegmentCode"]
      """  Segment value used to construct the GL Account.  """  
      self.SegmentNbr:int = obj["SegmentNbr"]
      self.RestrictDesc:str = obj["RestrictDesc"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class ChangeAllowed_input:
   """ Required : 
   currencyAcctType
   revalueOpt
   currencyCode
   allowed
   ds
   """  
   def __init__(self, obj):
      self.currencyAcctType:str = obj["currencyAcctType"]
      """  Currency Account Type  """  
      self.revalueOpt:int = obj["revalueOpt"]
      """  Revalue Option  """  
      self.currencyCode:str = obj["currencyCode"]
      """  Currency Code  """  
      self.allowed:bool = obj["allowed"]
      """  Allowed  """  
      self.ds:list[Erp_Tablesets_GLAccountMassUpdTableset] = obj["ds"]
      pass

class ChangeAllowed_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_GLAccountMassUpdTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeCurrencyAccount_input:
   """ Required : 
   coaCode
   revalueOpt
   ipValue
   ds
   """  
   def __init__(self, obj):
      self.coaCode:str = obj["coaCode"]
      """  Chart of account  """  
      self.revalueOpt:int = obj["revalueOpt"]
      """  Revalue option  """  
      self.ipValue:str = obj["ipValue"]
      """  Input value  """  
      self.ds:list[Erp_Tablesets_GLAccountMassUpdTableset] = obj["ds"]
      pass

class ChangeCurrencyAccount_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_GLAccountMassUpdTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeRevalue_input:
   """ Required : 
   revalueOpt
   currencyCode
   ds
   """  
   def __init__(self, obj):
      self.revalueOpt:int = obj["revalueOpt"]
      """  Revalue Option  """  
      self.currencyCode:str = obj["currencyCode"]
      """  Currency Code  """  
      self.ds:list[Erp_Tablesets_GLAccountMassUpdTableset] = obj["ds"]
      pass

class ChangeRevalue_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_GLAccountMassUpdTableset] = obj["ds"]
      pass

      """  output parameters  """  

class DefaultsOnAddSegAcct_input:
   """ Required : 
   glAccount
   accountDescField
   ds
   """  
   def __init__(self, obj):
      self.glAccount:str = obj["glAccount"]
      """  GL Account being processed  """  
      self.accountDescField:str = obj["accountDescField"]
      """  GL Account description field being updated  """  
      self.ds:list[Erp_Tablesets_GLAccountMassUpdTableset] = obj["ds"]
      pass

class DefaultsOnAddSegAcct_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_GLAccountMassUpdTableset] = obj["ds"]
      pass

      """  output parameters  """  

class DeleteByID_input:
   """ Required : 
   coACode
   """  
   def __init__(self, obj):
      self.coACode:str = obj["coACode"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class DeleteCurrencyAccount_input:
   """ Required : 
   coaCode
   currencyCode
   ds
   """  
   def __init__(self, obj):
      self.coaCode:str = obj["coaCode"]
      """  Chart of account  """  
      self.currencyCode:str = obj["currencyCode"]
      """  Currency code to delete  """  
      self.ds:list[Erp_Tablesets_GLAccountMassUpdTableset] = obj["ds"]
      pass

class DeleteCurrencyAccount_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_GLAccountMassUpdTableset] = obj["ds"]
      pass

      """  output parameters  """  

class Erp_Tablesets_COAListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.COACode:str = obj["COACode"]
      """  Chart of Account ID  """  
      self.Description:str = obj["Description"]
      """  The description or Name of this Chart of Accounts.  """  
      self.SeparatorChar:str = obj["SeparatorChar"]
      """  This is the character that is displayed between each segment of the GL Accounts.  Tilde (~~), Tick (`) and Vertical Bar (|) are invalid separators.  """  
      self.PerBalFmt:str = obj["PerBalFmt"]
      """  Internally used field.  Not intended for end-user use.  Tilde delimited string indicating the segments used in the period balance account.  Example: 1~2~5 indicates segments 1, 2 and 5 are used to construct the balance account number.  """  
      self.TBBalFmt:str = obj["TBBalFmt"]
      """  Internally used field.  Not intended for end-user use.  Tilde delimited string indicating the segments used in the trial balance account. Example: 1~3~4 indicates segments 1, 3 and 4 are used to construct the balance account number.  """  
      self.FmtChgDate:str = obj["FmtChgDate"]
      """  Internal field used by the GL Account Control to identify when cache needs to be updated with the new COA structure.  This is updated by the COASegment write and delete triggers.  It is not intended for end user use.  Only changes important to the GL Account control updates this field's value.  """  
      self.FmtChgTime:int = obj["FmtChgTime"]
      """  Internal field used by the GL Account Control to identify when cache needs to be updated with the new COA structure.  This is updated by the COASegment write and delete triggers.  It is not intended for end user use.  Only changes important to the GL Account control updates this field's value.  """  
      self.CtrlSegList:str = obj["CtrlSegList"]
      """  Internally used field.  Not intended for end-user use.  Tilde delimited string indicating the controlled segments.  Example: 1~2~5 indicates segments 1, 2 and 5 are controlled.  This field is to be used in those situations where reading all of the COASegements via the Dynamic index is too much overhead.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.GlobalCOA:bool = obj["GlobalCOA"]
      """  Marks the COA as Global  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Disables this record from receiving global updates  """  
      self.RebuildGLAccts:bool = obj["RebuildGLAccts"]
      """  Internal logical used by UI that indicates if GLAccounts exist for this COA and that the display gl account must be rebuilt  """  
      self.ChartInUse:bool = obj["ChartInUse"]
      """  Logical indicating if the chart has been used  """  
      self.ChartLength:int = obj["ChartLength"]
      """  Sum of the COASegment.MaxLength entries.  """  
      self.MasterCOA:bool = obj["MasterCOA"]
      """  Logical indicating if this COA is the Master COA.  """  
      self.NbrSegments:int = obj["NbrSegments"]
      """  Total number of segments defined for this COA  """  
      self.HasRefSegment:bool = obj["HasRefSegment"]
      """  logical indicating if this chart has a segment defined as use ref entity where the reference entity = GLCOARefType  """  
      self.ConsInUse:bool = obj["ConsInUse"]
      """  Logical indicating if this chart of accounts is subject to consolidation  """  
      self.RebuildBalances:bool = obj["RebuildBalances"]
      """  Logical indicating the balances are to be rebuilt due to a change in balance structure  """  
      self.CreateDefCat:bool = obj["CreateDefCat"]
      """  Logical indicating if default categories are to be created  """  
      self.GlbFlag:bool = obj["GlbFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_COARow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.COACode:str = obj["COACode"]
      """  Chart of Account ID  """  
      self.Description:str = obj["Description"]
      """  The description or Name of this Chart of Accounts.  """  
      self.SeparatorChar:str = obj["SeparatorChar"]
      """  This is the character that is displayed between each segment of the GL Accounts.  Tilde (~~), Tick (`) and Vertical Bar (|) are invalid separators.  """  
      self.PerBalFmt:str = obj["PerBalFmt"]
      """  Internally used field.  Not intended for end-user use.  Tilde delimited string indicating the segments used in the period balance account.  Example: 1~2~5 indicates segments 1, 2 and 5 are used to construct the balance account number.  """  
      self.TBBalFmt:str = obj["TBBalFmt"]
      """  Internally used field.  Not intended for end-user use.  Tilde delimited string indicating the segments used in the trial balance account. Example: 1~3~4 indicates segments 1, 3 and 4 are used to construct the balance account number.  """  
      self.FmtChgDate:str = obj["FmtChgDate"]
      """  Internal field used by the GL Account Control to identify when cache needs to be updated with the new COA structure.  This is updated by the COASegment write and delete triggers.  It is not intended for end user use.  Only changes important to the GL Account control updates this field's value.  """  
      self.FmtChgTime:int = obj["FmtChgTime"]
      """  Internal field used by the GL Account Control to identify when cache needs to be updated with the new COA structure.  This is updated by the COASegment write and delete triggers.  It is not intended for end user use.  Only changes important to the GL Account control updates this field's value.  """  
      self.CtrlSegList:str = obj["CtrlSegList"]
      """  Internally used field.  Not intended for end-user use.  Tilde delimited string indicating the controlled segments.  Example: 1~2~5 indicates segments 1, 2 and 5 are controlled.  This field is to be used in those situations where reading all of the COASegements via the Dynamic index is too much overhead.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.GlobalCOA:bool = obj["GlobalCOA"]
      """  Marks the COA as Global  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Disables this record from receiving global updates  """  
      self.RebuildGLAccts:bool = obj["RebuildGLAccts"]
      """  Internal logical used by UI that indicates if GLAccounts exist for this COA and that the display gl account must be rebuilt  """  
      self.PESunatCOA:str = obj["PESunatCOA"]
      """  Peru CSF: SUNAT Chart of Accounts Code  """  
      self.ChartInUse:bool = obj["ChartInUse"]
      """  Logical indicating if the chart has been used  """  
      self.CreateDefCat:bool = obj["CreateDefCat"]
      """  Logical indicating if default categories are to be created  """  
      self.EnableGlobalCOA:bool = obj["EnableGlobalCOA"]
      self.EnableGlobalLock:bool = obj["EnableGlobalLock"]
      self.GlbFlag:bool = obj["GlbFlag"]
      self.HasRefSegment:bool = obj["HasRefSegment"]
      """  logical indicating if this chart has a segment defined as use ref entity where the reference entity = GLCOARefType  """  
      self.MasterCOA:bool = obj["MasterCOA"]
      """  Logical indicating if this COA is the Master COA.  """  
      self.NbrSegments:int = obj["NbrSegments"]
      """  Total number of segments defined for this COA  """  
      self.RebuildBalances:bool = obj["RebuildBalances"]
      """  Logical indicating the balances are to be rebuilt due to a change in balance structure  """  
      self.ChartLength:int = obj["ChartLength"]
      """  Sum of the COASegment.MaxLength entries.  """  
      self.ConsInUse:bool = obj["ConsInUse"]
      """  Logical indicating if this chart of accounts is subject to consolidation  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_GLAccountMassUpdListTableset:
   def __init__(self, obj):
      self.COAList:list[Erp_Tablesets_COAListRow] = obj["COAList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_GLAccountMassUpdTableset:
   def __init__(self, obj):
      self.COA:list[Erp_Tablesets_COARow] = obj["COA"]
      self.SegAcct:list[Erp_Tablesets_SegAcctRow] = obj["SegAcct"]
      self.SegOpt:list[Erp_Tablesets_SegOptRow] = obj["SegOpt"]
      self.SegRange:list[Erp_Tablesets_SegRangeRow] = obj["SegRange"]
      self.SegRes:list[Erp_Tablesets_SegResRow] = obj["SegRes"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_NatAcctUpdCOACategoryRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.CategoryID:str = obj["CategoryID"]
      self.Description:str = obj["Description"]
      self.Type:str = obj["Type"]
      self.ParentCategory:str = obj["ParentCategory"]
      self.CatNumber:str = obj["CatNumber"]
      self.NumberOfParents:str = obj["NumberOfParents"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_NatAcctUpdCOACategoryTableset:
   def __init__(self, obj):
      self.NatAcctUpdCOACategory:list[Erp_Tablesets_NatAcctUpdCOACategoryRow] = obj["NatAcctUpdCOACategory"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_SegAcctRow:
   def __init__(self, obj):
      self.AccrualAccount:str = obj["AccrualAccount"]
      """  The natural account used as the accrual account.  """  
      self.AccrualGLDesc:str = obj["AccrualGLDesc"]
      """  Accrual GL Account description  """  
      self.AccrualSegVal1:str = obj["AccrualSegVal1"]
      """  AccrualSegVal1  """  
      self.AccrualSegVal10:str = obj["AccrualSegVal10"]
      """  AccrualSegVal10  """  
      self.AccrualSegVal11:str = obj["AccrualSegVal11"]
      """  AccrualSegVal11  """  
      self.AccrualSegVal12:str = obj["AccrualSegVal12"]
      """  AccrualSegVal12  """  
      self.AccrualSegVal13:str = obj["AccrualSegVal13"]
      """  AccrualSegVal13  """  
      self.AccrualSegVal14:str = obj["AccrualSegVal14"]
      """  AccrualSegVal14  """  
      self.AccrualSegVal15:str = obj["AccrualSegVal15"]
      """  AccrualSegVal15  """  
      self.AccrualSegVal16:str = obj["AccrualSegVal16"]
      """  AccrualSegVal16  """  
      self.AccrualSegVal17:str = obj["AccrualSegVal17"]
      """  AccrualSegVal17  """  
      self.AccrualSegVal18:str = obj["AccrualSegVal18"]
      """  AccrualSegVal18  """  
      self.AccrualSegVal19:str = obj["AccrualSegVal19"]
      """  AccrualSegVal19  """  
      self.AccrualSegVal2:str = obj["AccrualSegVal2"]
      """  AccrualSegVal2  """  
      self.AccrualSegVal20:str = obj["AccrualSegVal20"]
      """  AccrualSegVal20  """  
      self.AccrualSegVal3:str = obj["AccrualSegVal3"]
      """  AccrualSegVal3  """  
      self.AccrualSegVal4:str = obj["AccrualSegVal4"]
      """  AccrualSegVal4  """  
      self.AccrualSegVal5:str = obj["AccrualSegVal5"]
      """  AccrualSegVal5  """  
      self.AccrualSegVal6:str = obj["AccrualSegVal6"]
      """  AccrualSegVal6  """  
      self.AccrualSegVal7:str = obj["AccrualSegVal7"]
      """  AccrualSegVal7  """  
      self.AccrualSegVal8:str = obj["AccrualSegVal8"]
      """  AccrualSegVal8  """  
      self.AccrualSegVal9:str = obj["AccrualSegVal9"]
      """  AccrualSegVal9  """  
      self.Allowed:bool = obj["Allowed"]
      """  Indicates the currency can be used as a transactional currency.  """  
      self.COACode:str = obj["COACode"]
      """  Chart of Account ID  """  
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.CurrDesc:str = obj["CurrDesc"]
      """  Description of the currency  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  Unique code identifying the currency.  Only those values defined in the CurrencyMaster are allowed.  """  
      self.CurrencyID:str = obj["CurrencyID"]
      """  This is the updatable version of CurrencyCode.  This currency cannot be a record already in the currency table.  """  
      self.CurrName:str = obj["CurrName"]
      """   Used to print as the suffix to the word amount line printed on checks.  For example:
One Hundred and 00/100 Dollars. In this case  "Dollars" is the CurrName  """  
      self.CurrSymbol:str = obj["CurrSymbol"]
      """  A symbol that identifies the currency. Used on Forms and displays  """  
      self.DocumentDesc:str = obj["DocumentDesc"]
      """   An extended description that can be used on documents such as
POs and invoices.  """  
      self.GainAccount:str = obj["GainAccount"]
      """  The natural account used for booking currency gains.  """  
      self.GainGLDesc:str = obj["GainGLDesc"]
      """  Gain GL Account Description  """  
      self.GainSegVal1:str = obj["GainSegVal1"]
      """  GainSegVal1  """  
      self.GainSegVal10:str = obj["GainSegVal10"]
      """  GainSegVal10  """  
      self.GainSegVal11:str = obj["GainSegVal11"]
      """  GainSegVal11  """  
      self.GainSegVal12:str = obj["GainSegVal12"]
      """  GainSegVal12  """  
      self.GainSegVal13:str = obj["GainSegVal13"]
      """  GainSegVal13  """  
      self.GainSegVal14:str = obj["GainSegVal14"]
      """  GainSegVal14  """  
      self.GainSegVal15:str = obj["GainSegVal15"]
      """  GainSegVal15  """  
      self.GainSegVal16:str = obj["GainSegVal16"]
      """  GainSegVal16  """  
      self.GainSegVal17:str = obj["GainSegVal17"]
      """  GainSegVal17  """  
      self.GainSegVal18:str = obj["GainSegVal18"]
      """  GainSegVal18  """  
      self.GainSegVal19:str = obj["GainSegVal19"]
      """  GainSegVal19  """  
      self.GainSegVal2:str = obj["GainSegVal2"]
      """  GainSegVal2  """  
      self.GainSegVal20:str = obj["GainSegVal20"]
      """  GainSegVal20  """  
      self.GainSegVal3:str = obj["GainSegVal3"]
      """  GainSegVal3  """  
      self.GainSegVal4:str = obj["GainSegVal4"]
      """  GainSegVal4  """  
      self.GainSegVal5:str = obj["GainSegVal5"]
      """  GainSegVal5  """  
      self.GainSegVal6:str = obj["GainSegVal6"]
      """  GainSegVal6  """  
      self.GainSegVal7:str = obj["GainSegVal7"]
      """  GainSegVal7  """  
      self.GainSegVal8:str = obj["GainSegVal8"]
      """  GainSegVal8  """  
      self.GainSegVal9:str = obj["GainSegVal9"]
      """  GainSegVal9  """  
      self.LossAccount:str = obj["LossAccount"]
      """  The natural account used for booking currency losses.  """  
      self.LossGLDesc:str = obj["LossGLDesc"]
      """  Loss GL Account Description  """  
      self.LossSegVal1:str = obj["LossSegVal1"]
      """  LossSegVal1  """  
      self.LossSegVal10:str = obj["LossSegVal10"]
      """  LossSegVal10  """  
      self.LossSegVal11:str = obj["LossSegVal11"]
      """  LossSegVal11  """  
      self.LossSegVal12:str = obj["LossSegVal12"]
      """  LossSegVal12  """  
      self.LossSegVal13:str = obj["LossSegVal13"]
      """  LossSegVal13  """  
      self.LossSegVal14:str = obj["LossSegVal14"]
      """  LossSegVal14  """  
      self.LossSegVal15:str = obj["LossSegVal15"]
      """  LossSegVal15  """  
      self.LossSegVal16:str = obj["LossSegVal16"]
      """  LossSegVal16  """  
      self.LossSegVal17:str = obj["LossSegVal17"]
      """  LossSegVal17  """  
      self.LossSegVal18:str = obj["LossSegVal18"]
      """  LossSegVal18  """  
      self.LossSegVal19:str = obj["LossSegVal19"]
      """  LossSegVal19  """  
      self.LossSegVal2:str = obj["LossSegVal2"]
      """  LossSegVal2  """  
      self.LossSegVal20:str = obj["LossSegVal20"]
      """  LossSegVal20  """  
      self.LossSegVal3:str = obj["LossSegVal3"]
      """  LossSegVal3  """  
      self.LossSegVal4:str = obj["LossSegVal4"]
      """  LossSegVal4  """  
      self.LossSegVal5:str = obj["LossSegVal5"]
      """  LossSegVal5  """  
      self.LossSegVal6:str = obj["LossSegVal6"]
      """  LossSegVal6  """  
      self.LossSegVal7:str = obj["LossSegVal7"]
      """  LossSegVal7  """  
      self.LossSegVal8:str = obj["LossSegVal8"]
      """  LossSegVal8  """  
      self.LossSegVal9:str = obj["LossSegVal9"]
      """  LossSegVal9  """  
      self.Revalue:int = obj["Revalue"]
      """   Indicates if the transaction currency amount can be revalued.  Valid values are:
0 - no revalulation (deafult)
1 - only profits
2 - only losses
3 - both profit and losses  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_SegOptRow:
   def __init__(self, obj):
      self.COACode:str = obj["COACode"]
      """  Chart of Account ID  """  
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.DefaultSegment:str = obj["DefaultSegment"]
      """  Indicates the default segment value to be used for this natural account.  """  
      self.SegmentCode:str = obj["SegmentCode"]
      """  Segment value used to construct the GL Account.  """  
      self.ValOption:str = obj["ValOption"]
      """   Indicates if a segment is used for the natural account.  Valid values are:
M - Mandatory
O - Optional
N - Not Used  """  
      self.SegmentName:str = obj["SegmentName"]
      self.SegmentNbr:int = obj["SegmentNbr"]
      self.SubSegmentNbr:int = obj["SubSegmentNbr"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_SegRangeRow:
   def __init__(self, obj):
      self.COACode:str = obj["COACode"]
      """  Chart of Account ID  """  
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.EndVal:str = obj["EndVal"]
      self.RangeID:str = obj["RangeID"]
      """  From code to code  """  
      self.SegmentNbr:int = obj["SegmentNbr"]
      self.StartVal:str = obj["StartVal"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_SegResRow:
   def __init__(self, obj):
      self.COACode:str = obj["COACode"]
      """  Chart of Account ID  """  
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.FctBlocked:bool = obj["FctBlocked"]
      """  Indicates if GL Account entry is prohibited  """  
      self.RestrictID:str = obj["RestrictID"]
      """  Application DLL name  """  
      self.SegmentCode:str = obj["SegmentCode"]
      """  Segment value used to construct the GL Account.  """  
      self.SegmentNbr:int = obj["SegmentNbr"]
      self.RestrictDesc:str = obj["RestrictDesc"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_UpdExtGLAccountMassUpdTableset:
   def __init__(self, obj):
      self.COA:list[Erp_Tablesets_COARow] = obj["COA"]
      self.SegAcct:list[Erp_Tablesets_SegAcctRow] = obj["SegAcct"]
      self.SegOpt:list[Erp_Tablesets_SegOptRow] = obj["SegOpt"]
      self.SegRange:list[Erp_Tablesets_SegRangeRow] = obj["SegRange"]
      self.SegRes:list[Erp_Tablesets_SegResRow] = obj["SegRes"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetByID_input:
   """ Required : 
   coACode
   """  
   def __init__(self, obj):
      self.coACode:str = obj["coACode"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_GLAccountMassUpdTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_GLAccountMassUpdTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_GLAccountMassUpdTableset] = obj["returnObj"]
      pass

class GetCOACategoriesFromList_input:
   """ Required : 
   categoryList
   """  
   def __init__(self, obj):
      self.categoryList:str = obj["categoryList"]
      """  Category list  """  
      pass

class GetCOACategoriesFromList_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_NatAcctUpdCOACategoryTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_GLAccountMassUpdListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetListsForProcess_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_GLAccountMassUpdTableset] = obj["ds"]
      pass

class GetListsForProcess_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.segRangesList:str = obj["parameters"]
      self.segOptsList:str = obj["parameters"]
      self.restrictionsList:str = obj["parameters"]
      self.coaSegAcctList:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetNewCOA_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_GLAccountMassUpdTableset] = obj["ds"]
      pass

class GetNewCOA_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_GLAccountMassUpdTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewSegOpt_input:
   """ Required : 
   coaCode
   ds
   """  
   def __init__(self, obj):
      self.coaCode:str = obj["coaCode"]
      """  COA Code  """  
      self.ds:list[Erp_Tablesets_GLAccountMassUpdTableset] = obj["ds"]
      pass

class GetNewSegOpt_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_GLAccountMassUpdTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewSegRange_input:
   """ Required : 
   coaCode
   ds
   """  
   def __init__(self, obj):
      self.coaCode:str = obj["coaCode"]
      """  COA Code  """  
      self.ds:list[Erp_Tablesets_GLAccountMassUpdTableset] = obj["ds"]
      pass

class GetNewSegRange_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_GLAccountMassUpdTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewSegRes_input:
   """ Required : 
   coaCode
   ds
   """  
   def __init__(self, obj):
      self.coaCode:str = obj["coaCode"]
      """  COA Code  """  
      self.ds:list[Erp_Tablesets_GLAccountMassUpdTableset] = obj["ds"]
      pass

class GetNewSegRes_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_GLAccountMassUpdTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseCOA
   whereClauseSegAcct
   whereClauseSegOpt
   whereClauseSegRange
   whereClauseSegRes
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseCOA:str = obj["whereClauseCOA"]
      self.whereClauseSegAcct:str = obj["whereClauseSegAcct"]
      self.whereClauseSegOpt:str = obj["whereClauseSegOpt"]
      self.whereClauseSegRange:str = obj["whereClauseSegRange"]
      self.whereClauseSegRes:str = obj["whereClauseSegRes"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_GLAccountMassUpdTableset] = obj["returnObj"]
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
      self.ds:list[Erp_Tablesets_UpdExtGLAccountMassUpdTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtGLAccountMassUpdTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_GLAccountMassUpdTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_GLAccountMassUpdTableset] = obj["ds"]
      pass

      """  output parameters  """  

