import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.COASegValuesSvc
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.COASegValuesSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.COASegValuesSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_COASegValues(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get COASegValues items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_COASegValues
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.COASegValuesRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.COASegValuesSvc/COASegValues",headers=creds) as resp:
           return await resp.json()

async def post_COASegValues(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_COASegValues
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.COASegValuesRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.COASegValuesRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.COASegValuesSvc/COASegValues", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_COASegValues_Company_COACode_SegmentNbr_SegmentCode(Company, COACode, SegmentNbr, SegmentCode, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the COASegValue item
   Description: Calls GetByID to retrieve the COASegValue item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_COASegValue
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param COACode: Desc: COACode   Required: True   Allow empty value : True
      :param SegmentNbr: Desc: SegmentNbr   Required: True
      :param SegmentCode: Desc: SegmentCode   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.COASegValuesRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.COASegValuesSvc/COASegValues(" + Company + "," + COACode + "," + SegmentNbr + "," + SegmentCode + ")",headers=creds) as resp:
           return await resp.json()

async def patch_COASegValues_Company_COACode_SegmentNbr_SegmentCode(Company, COACode, SegmentNbr, SegmentCode, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update COASegValue for the service
   Description: Calls UpdateExt to update COASegValue. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_COASegValue
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param COACode: Desc: COACode   Required: True   Allow empty value : True
      :param SegmentNbr: Desc: SegmentNbr   Required: True
      :param SegmentCode: Desc: SegmentCode   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.COASegValuesRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.COASegValuesSvc/COASegValues(" + Company + "," + COACode + "," + SegmentNbr + "," + SegmentCode + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_COASegValues_Company_COACode_SegmentNbr_SegmentCode(Company, COACode, SegmentNbr, SegmentCode, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete COASegValue item
   Description: Call UpdateExt to delete COASegValue item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_COASegValue
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param COACode: Desc: COACode   Required: True   Allow empty value : True
      :param SegmentNbr: Desc: SegmentNbr   Required: True
      :param SegmentCode: Desc: SegmentCode   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.COASegValuesSvc/COASegValues(" + Company + "," + COACode + "," + SegmentNbr + "," + SegmentCode + ")",headers=creds) as resp:
           return await resp.json()

async def get_COASegValues_Company_COACode_SegmentNbr_SegmentCode_COASegAccts(Company, COACode, SegmentNbr, SegmentCode, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get COASegAccts items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_COASegAccts1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param COACode: Desc: COACode   Required: True   Allow empty value : True
      :param SegmentNbr: Desc: SegmentNbr   Required: True
      :param SegmentCode: Desc: SegmentCode   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.COASegAcctRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.COASegValuesSvc/COASegValues(" + Company + "," + COACode + "," + SegmentNbr + "," + SegmentCode + ")/COASegAccts",headers=creds) as resp:
           return await resp.json()

async def get_COASegValues_Company_COACode_SegmentNbr_SegmentCode_COASegAccts_Company_COACode_SegmentNbr_SegmentCode_CurrencyCode(Company, COACode, SegmentNbr, SegmentCode, CurrencyCode, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the COASegAcct item
   Description: Calls GetByID to retrieve the COASegAcct item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_COASegAcct1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param COACode: Desc: COACode   Required: True   Allow empty value : True
      :param SegmentNbr: Desc: SegmentNbr   Required: True
      :param SegmentCode: Desc: SegmentCode   Required: True   Allow empty value : True
      :param CurrencyCode: Desc: CurrencyCode   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.COASegAcctRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.COASegValuesSvc/COASegValues(" + Company + "," + COACode + "," + SegmentNbr + "," + SegmentCode + ")/COASegAccts(" + Company + "," + COACode + "," + SegmentNbr + "," + SegmentCode + "," + CurrencyCode + ")",headers=creds) as resp:
           return await resp.json()

async def get_COASegValues_Company_COACode_SegmentNbr_SegmentCode_COASegOpts(Company, COACode, SegmentNbr, SegmentCode, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get COASegOpts items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_COASegOpts1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param COACode: Desc: COACode   Required: True   Allow empty value : True
      :param SegmentNbr: Desc: SegmentNbr   Required: True
      :param SegmentCode: Desc: SegmentCode   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.COASegOptRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.COASegValuesSvc/COASegValues(" + Company + "," + COACode + "," + SegmentNbr + "," + SegmentCode + ")/COASegOpts",headers=creds) as resp:
           return await resp.json()

async def get_COASegValues_Company_COACode_SegmentNbr_SegmentCode_COASegOpts_Company_COACode_SegmentNbr_SegmentCode_SubSegmentNbr(Company, COACode, SegmentNbr, SegmentCode, SubSegmentNbr, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the COASegOpt item
   Description: Calls GetByID to retrieve the COASegOpt item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_COASegOpt1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param COACode: Desc: COACode   Required: True   Allow empty value : True
      :param SegmentNbr: Desc: SegmentNbr   Required: True
      :param SegmentCode: Desc: SegmentCode   Required: True   Allow empty value : True
      :param SubSegmentNbr: Desc: SubSegmentNbr   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.COASegOptRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.COASegValuesSvc/COASegValues(" + Company + "," + COACode + "," + SegmentNbr + "," + SegmentCode + ")/COASegOpts(" + Company + "," + COACode + "," + SegmentNbr + "," + SegmentCode + "," + SubSegmentNbr + ")",headers=creds) as resp:
           return await resp.json()

async def get_COASegValues_Company_COACode_SegmentNbr_SegmentCode_COASegRes(Company, COACode, SegmentNbr, SegmentCode, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get COASegRes items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_COASegRes1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param COACode: Desc: COACode   Required: True   Allow empty value : True
      :param SegmentNbr: Desc: SegmentNbr   Required: True
      :param SegmentCode: Desc: SegmentCode   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.COASegResRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.COASegValuesSvc/COASegValues(" + Company + "," + COACode + "," + SegmentNbr + "," + SegmentCode + ")/COASegRes",headers=creds) as resp:
           return await resp.json()

async def get_COASegValues_Company_COACode_SegmentNbr_SegmentCode_COASegRes_Company_COACode_SegmentNbr_SegmentCode_RestrictID(Company, COACode, SegmentNbr, SegmentCode, RestrictID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the COASegRe item
   Description: Calls GetByID to retrieve the COASegRe item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_COASegRe1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param COACode: Desc: COACode   Required: True   Allow empty value : True
      :param SegmentNbr: Desc: SegmentNbr   Required: True
      :param SegmentCode: Desc: SegmentCode   Required: True   Allow empty value : True
      :param RestrictID: Desc: RestrictID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.COASegResRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.COASegValuesSvc/COASegValues(" + Company + "," + COACode + "," + SegmentNbr + "," + SegmentCode + ")/COASegRes(" + Company + "," + COACode + "," + SegmentNbr + "," + SegmentCode + "," + RestrictID + ")",headers=creds) as resp:
           return await resp.json()

async def get_COASegAccts(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get COASegAccts items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_COASegAccts
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.COASegAcctRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.COASegValuesSvc/COASegAccts",headers=creds) as resp:
           return await resp.json()

async def post_COASegAccts(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_COASegAccts
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.COASegAcctRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.COASegAcctRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.COASegValuesSvc/COASegAccts", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_COASegAccts_Company_COACode_SegmentNbr_SegmentCode_CurrencyCode(Company, COACode, SegmentNbr, SegmentCode, CurrencyCode, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the COASegAcct item
   Description: Calls GetByID to retrieve the COASegAcct item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_COASegAcct
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param COACode: Desc: COACode   Required: True   Allow empty value : True
      :param SegmentNbr: Desc: SegmentNbr   Required: True
      :param SegmentCode: Desc: SegmentCode   Required: True   Allow empty value : True
      :param CurrencyCode: Desc: CurrencyCode   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.COASegAcctRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.COASegValuesSvc/COASegAccts(" + Company + "," + COACode + "," + SegmentNbr + "," + SegmentCode + "," + CurrencyCode + ")",headers=creds) as resp:
           return await resp.json()

async def patch_COASegAccts_Company_COACode_SegmentNbr_SegmentCode_CurrencyCode(Company, COACode, SegmentNbr, SegmentCode, CurrencyCode, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update COASegAcct for the service
   Description: Calls UpdateExt to update COASegAcct. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_COASegAcct
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param COACode: Desc: COACode   Required: True   Allow empty value : True
      :param SegmentNbr: Desc: SegmentNbr   Required: True
      :param SegmentCode: Desc: SegmentCode   Required: True   Allow empty value : True
      :param CurrencyCode: Desc: CurrencyCode   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.COASegAcctRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.COASegValuesSvc/COASegAccts(" + Company + "," + COACode + "," + SegmentNbr + "," + SegmentCode + "," + CurrencyCode + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_COASegAccts_Company_COACode_SegmentNbr_SegmentCode_CurrencyCode(Company, COACode, SegmentNbr, SegmentCode, CurrencyCode, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete COASegAcct item
   Description: Call UpdateExt to delete COASegAcct item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_COASegAcct
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param COACode: Desc: COACode   Required: True   Allow empty value : True
      :param SegmentNbr: Desc: SegmentNbr   Required: True
      :param SegmentCode: Desc: SegmentCode   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.COASegValuesSvc/COASegAccts(" + Company + "," + COACode + "," + SegmentNbr + "," + SegmentCode + "," + CurrencyCode + ")",headers=creds) as resp:
           return await resp.json()

async def get_COASegOpts(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get COASegOpts items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_COASegOpts
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.COASegOptRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.COASegValuesSvc/COASegOpts",headers=creds) as resp:
           return await resp.json()

async def post_COASegOpts(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_COASegOpts
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.COASegOptRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.COASegOptRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.COASegValuesSvc/COASegOpts", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_COASegOpts_Company_COACode_SegmentNbr_SegmentCode_SubSegmentNbr(Company, COACode, SegmentNbr, SegmentCode, SubSegmentNbr, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the COASegOpt item
   Description: Calls GetByID to retrieve the COASegOpt item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_COASegOpt
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param COACode: Desc: COACode   Required: True   Allow empty value : True
      :param SegmentNbr: Desc: SegmentNbr   Required: True
      :param SegmentCode: Desc: SegmentCode   Required: True   Allow empty value : True
      :param SubSegmentNbr: Desc: SubSegmentNbr   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.COASegOptRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.COASegValuesSvc/COASegOpts(" + Company + "," + COACode + "," + SegmentNbr + "," + SegmentCode + "," + SubSegmentNbr + ")",headers=creds) as resp:
           return await resp.json()

async def patch_COASegOpts_Company_COACode_SegmentNbr_SegmentCode_SubSegmentNbr(Company, COACode, SegmentNbr, SegmentCode, SubSegmentNbr, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update COASegOpt for the service
   Description: Calls UpdateExt to update COASegOpt. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_COASegOpt
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param COACode: Desc: COACode   Required: True   Allow empty value : True
      :param SegmentNbr: Desc: SegmentNbr   Required: True
      :param SegmentCode: Desc: SegmentCode   Required: True   Allow empty value : True
      :param SubSegmentNbr: Desc: SubSegmentNbr   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.COASegOptRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.COASegValuesSvc/COASegOpts(" + Company + "," + COACode + "," + SegmentNbr + "," + SegmentCode + "," + SubSegmentNbr + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_COASegOpts_Company_COACode_SegmentNbr_SegmentCode_SubSegmentNbr(Company, COACode, SegmentNbr, SegmentCode, SubSegmentNbr, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete COASegOpt item
   Description: Call UpdateExt to delete COASegOpt item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_COASegOpt
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param COACode: Desc: COACode   Required: True   Allow empty value : True
      :param SegmentNbr: Desc: SegmentNbr   Required: True
      :param SegmentCode: Desc: SegmentCode   Required: True   Allow empty value : True
      :param SubSegmentNbr: Desc: SubSegmentNbr   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.COASegValuesSvc/COASegOpts(" + Company + "," + COACode + "," + SegmentNbr + "," + SegmentCode + "," + SubSegmentNbr + ")",headers=creds) as resp:
           return await resp.json()

async def get_COASegRes(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get COASegRes items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_COASegRes
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.COASegResRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.COASegValuesSvc/COASegRes",headers=creds) as resp:
           return await resp.json()

async def post_COASegRes(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_COASegRes
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.COASegResRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.COASegResRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.COASegValuesSvc/COASegRes", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_COASegRes_Company_COACode_SegmentNbr_SegmentCode_RestrictID(Company, COACode, SegmentNbr, SegmentCode, RestrictID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the COASegRe item
   Description: Calls GetByID to retrieve the COASegRe item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_COASegRe
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param COACode: Desc: COACode   Required: True   Allow empty value : True
      :param SegmentNbr: Desc: SegmentNbr   Required: True
      :param SegmentCode: Desc: SegmentCode   Required: True   Allow empty value : True
      :param RestrictID: Desc: RestrictID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.COASegResRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.COASegValuesSvc/COASegRes(" + Company + "," + COACode + "," + SegmentNbr + "," + SegmentCode + "," + RestrictID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_COASegRes_Company_COACode_SegmentNbr_SegmentCode_RestrictID(Company, COACode, SegmentNbr, SegmentCode, RestrictID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update COASegRe for the service
   Description: Calls UpdateExt to update COASegRe. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_COASegRe
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param COACode: Desc: COACode   Required: True   Allow empty value : True
      :param SegmentNbr: Desc: SegmentNbr   Required: True
      :param SegmentCode: Desc: SegmentCode   Required: True   Allow empty value : True
      :param RestrictID: Desc: RestrictID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.COASegResRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.COASegValuesSvc/COASegRes(" + Company + "," + COACode + "," + SegmentNbr + "," + SegmentCode + "," + RestrictID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_COASegRes_Company_COACode_SegmentNbr_SegmentCode_RestrictID(Company, COACode, SegmentNbr, SegmentCode, RestrictID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete COASegRe item
   Description: Call UpdateExt to delete COASegRe item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_COASegRe
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param COACode: Desc: COACode   Required: True   Allow empty value : True
      :param SegmentNbr: Desc: SegmentNbr   Required: True
      :param SegmentCode: Desc: SegmentCode   Required: True   Allow empty value : True
      :param RestrictID: Desc: RestrictID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.COASegValuesSvc/COASegRes(" + Company + "," + COACode + "," + SegmentNbr + "," + SegmentCode + "," + RestrictID + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.COASegValuesListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.COASegValuesSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseCOASegValues, whereClauseCOASegAcct, whereClauseCOASegOpt, whereClauseCOASegRes, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClauseCOASegValues=" + whereClauseCOASegValues
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseCOASegAcct=" + whereClauseCOASegAcct
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseCOASegOpt=" + whereClauseCOASegOpt
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseCOASegRes=" + whereClauseCOASegRes
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.COASegValuesSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(coACode, segmentNbr, segmentCode, epicorHeaders = None):
   """  
   Summary: Invoke method GetByID
   Description: Returns a DataSet given the primary key.
   OperationID: Get_GetByID
   Required: True   Allow empty value : True
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
   params += "coACode=" + coACode
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "segmentNbr=" + segmentNbr
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "segmentCode=" + segmentCode

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.COASegValuesSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.COASegValuesSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_ChangeRevalueOpt(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeRevalueOpt
   Description: On Revalue Option change
   OperationID: ChangeRevalueOpt
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeRevalueOpt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeRevalueOpt_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.COASegValuesSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeRateType(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeRateType
   Description: On Rate Type changing
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.COASegValuesSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeAccountContext(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeAccountContext
   Description: On Account context changing
   OperationID: ChangeAccountContext
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeAccountContext_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeAccountContext_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.COASegValuesSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeAllowed(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeAllowed
   Description: On allowed change this method evaluates the Currency account type option to handle proper functionality.
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.COASegValuesSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeCategory(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeCategory
   Description: This method convert the document currency to the journal currency.
   OperationID: ChangeCategory
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeCategory_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeCategory_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.COASegValuesSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeCurrencyAccount(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeCurrencyAccount
   Description: On currency account change, all related currencies should be updated to allowed/not allowed
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.COASegValuesSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeSegvalue(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeSegvalue
   OperationID: ChangeSegvalue
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeSegvalue_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeSegvalue_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.COASegValuesSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckForDupSegOpt(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckForDupSegOpt
   Description: Purpose: Make sure a COASegment has not been entered twice for a given segment value.
The ipSubSegmentNbr is the sub segment number to look for in the COASegOpt table.
The segment number to search on is one since these options are only valid for the
natural account and the natural account is ALWAYS segment number 1.
Parameters:
<param name="ipCOACode"> COA Code</param><param name="ipSubSegmentNbr"> Segment Number to check for existence</param><param name="ipSegmentCode">Segment Code to search for </param>
Notes:
   OperationID: CheckForDupSegOpt
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckForDupSegOpt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckForDupSegOpt_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.COASegValuesSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeStatistical(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeStatistical
   OperationID: ChangeStatistical
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeStatistical_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeStatistical_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.COASegValuesSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeStatisticalOnly(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeStatisticalOnly
   OperationID: ChangeStatisticalOnly
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeStatisticalOnly_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeStatisticalOnly_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.COASegValuesSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeStatUOMCode(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeStatUOMCode
   OperationID: ChangeStatUOMCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeStatUOMCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeStatUOMCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.COASegValuesSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeLinkedPlant(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeLinkedPlant
   OperationID: ChangeLinkedPlant
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeLinkedPlant_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeLinkedPlant_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.COASegValuesSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeActive(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeActive
   Description: Change Active related validations.
   OperationID: ChangeActive
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeActive_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeActive_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.COASegValuesSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_COASegValueActiveFlagChanging(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method COASegValueActiveFlagChanging
   Description: Performs validations when changing ActiveFlag
Checks for GL Control references when marking a segment value as inactive
   OperationID: COASegValueActiveFlagChanging
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/COASegValueActiveFlagChanging_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/COASegValueActiveFlagChanging_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.COASegValuesSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_RemoveSiteSegmentCodeDuplicate(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method RemoveSiteSegmentCodeDuplicate
   Description: SegmentCode duplicate values should be removed.
   OperationID: RemoveSiteSegmentCodeDuplicate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/RemoveSiteSegmentCodeDuplicate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RemoveSiteSegmentCodeDuplicate_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.COASegValuesSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeSiteSegmentCode(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeSiteSegmentCode
   Description: Validates new Site Segment Code value
   OperationID: ChangeSiteSegmentCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeSiteSegmentCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeSiteSegmentCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.COASegValuesSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_SiteSegmentChanged(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method SiteSegmentChanged
   Description: Populates info about selected segment value
   OperationID: SiteSegmentChanged
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SiteSegmentChanged_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SiteSegmentChanged_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.COASegValuesSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChgStatUOMCode(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChgStatUOMCode
   OperationID: ChgStatUOMCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChgStatUOMCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChgStatUOMCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.COASegValuesSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetCOASegmentGlobalFields(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetCOASegmentGlobalFields
   Description: none
   OperationID: GetCOASegmentGlobalFields
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetCOASegmentGlobalFields_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCOASegmentGlobalFields_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.COASegValuesSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ComboValues(epicorHeaders = None):
   """  
   Summary: Invoke method ComboValues
   Description: Purpose:Used to setup the initial values of the combos placed on the Header
            
Parameters:
<param name="opCOACode">Indicates the COACODE the Chart of Accounts</param><param name="opDescription">Indicates the Description on fo the COACODE</param><param name="opSegmentNbr">Indicates Segment number of the Segment</param><param name="opSegmentName">Indicates the Segment Name of the Segment</param><param name="opGlobalCOA">opGlobalCOA</param><param name="opGlobalSegment">opGlobalSegment </param>
Notes:
   OperationID: ComboValues
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/ComboValues_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.COASegValuesSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_ValidateCOACodeSite(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateCOACodeSite
   Description: returns a description and Global COA flags of the entered COA code with Site Segment info
   OperationID: ValidateCOACodeSite
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateCOACodeSite_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateCOACodeSite_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.COASegValuesSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidateCOACode(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateCOACode
   Description: returns a description and Global COA flags of the entered COA code
   OperationID: ValidateCOACode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateCOACode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateCOACode_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.COASegValuesSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidateCOASegment(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateCOASegment
   Description: Validate segment number
   OperationID: ValidateCOASegment
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateCOASegment_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateCOASegment_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.COASegValuesSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetListCBOnly(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetListCBOnly
   Description: Purpose:
Parameters:
<param name="WhereClause">COASegValues search clause</param><param name="pageSize">Page size</param><param name="absolutePage">Absolute page</param><param name="morePages">More Pages</param>
Notes:
   OperationID: GetListCBOnly
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetListCBOnly_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetListCBOnly_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.COASegValuesSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidateCurrencyAccount(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateCurrencyAccount
   Description: Purpose:
Parameters:
<param name="ipCOACode">COA code</param><param name="ipSegmentCode">segment code</param><param name="ipCurrencyAcct">flag identifying the segment as a currency account</param><param name="CurrencyAcctType">currency account Type</param>
Notes:
   OperationID: ValidateCurrencyAccount
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateCurrencyAccount_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateCurrencyAccount_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.COASegValuesSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidateDefaultSegment(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateDefaultSegment
   Description: Purpose:
Parameters:
<param name="ipCOACode"> COA Code</param><param name="ipSubSegmentNbr"> Segment Number to check for existence</param><param name="ipSegmentCode">Segment Code to search for </param>
Notes:
   OperationID: ValidateDefaultSegment
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateDefaultSegment_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateDefaultSegment_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.COASegValuesSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DefaultsOnAdd(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DefaultsOnAdd
   Description: Set Default creating a new account
   OperationID: DefaultsOnAdd
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DefaultsOnAdd_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DefaultsOnAdd_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.COASegValuesSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DefaultsOnAddSegAcct(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DefaultsOnAddSegAcct
   Description: Set Default creating a new COASegAcct
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.COASegValuesSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DeleteTransactionCurrencies(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DeleteTransactionCurrencies
   Description: Delete Transaction Currencies
   OperationID: DeleteTransactionCurrencies
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DeleteTransactionCurrencies_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteTransactionCurrencies_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.COASegValuesSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_IsStatOnlySegment(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method IsStatOnlySegment
   OperationID: IsStatOnlySegment
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/IsStatOnlySegment_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/IsStatOnlySegment_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.COASegValuesSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_getBookRevOpt(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method getBookRevOpt
   OperationID: getBookRevOpt
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/getBookRevOpt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/getBookRevOpt_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.COASegValuesSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckCOASeparatorInSegmentValue(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckCOASeparatorInSegmentValue
   Description: Return warning message if Segment Value contains COA Separator
   OperationID: CheckCOASeparatorInSegmentValue
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckCOASeparatorInSegmentValue_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckCOASeparatorInSegmentValue_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.COASegValuesSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GenerateSiteSegmentSetupData(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GenerateSiteSegmentSetupData
   OperationID: GenerateSiteSegmentSetupData
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GenerateSiteSegmentSetupData_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GenerateSiteSegmentSetupData_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.COASegValuesSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetSiteSetting(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetSiteSetting
   Description: Site Segment wizard availability
   OperationID: GetSiteSetting
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetSiteSetting_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetSiteSetting_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.COASegValuesSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DefaultBookID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DefaultBookID
   Description: Returns the default book value.
   OperationID: DefaultBookID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DefaultBookID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DefaultBookID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.COASegValuesSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetInterSiteAccountPairs(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetInterSiteAccountPairs
   Description: Returns intersite account pairs for due from/due to
   OperationID: GetInterSiteAccountPairs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetInterSiteAccountPairs_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetInterSiteAccountPairs_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.COASegValuesSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_IntersiteAccountPairsApply(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method IntersiteAccountPairsApply
   Description: Apply due from/due to account pairs
   OperationID: IntersiteAccountPairsApply
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/IntersiteAccountPairsApply_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/IntersiteAccountPairsApply_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.COASegValuesSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetSiteSegmentSetupData(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetSiteSegmentSetupData
   Description: Generates data for Site Segment Setup Wizard
   OperationID: GetSiteSegmentSetupData
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetSiteSegmentSetupData_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetSiteSegmentSetupData_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.COASegValuesSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_SiteSegmentSetupApply(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method SiteSegmentSetupApply
   Description: Applies Site Segment info for segment values
   OperationID: SiteSegmentSetupApply
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SiteSegmentSetupApply_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SiteSegmentSetupApply_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.COASegValuesSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewCOASegValues(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewCOASegValues
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewCOASegValues
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewCOASegValues_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewCOASegValues_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.COASegValuesSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewCOASegAcct(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewCOASegAcct
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewCOASegAcct
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewCOASegAcct_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewCOASegAcct_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.COASegValuesSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewCOASegOpt(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewCOASegOpt
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewCOASegOpt
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewCOASegOpt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewCOASegOpt_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.COASegValuesSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewCOASegRes(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewCOASegRes
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewCOASegRes
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewCOASegRes_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewCOASegRes_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.COASegValuesSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.COASegValuesSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.COASegValuesSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.COASegValuesSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.COASegValuesSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.COASegValuesSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_COASegAcctRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_COASegAcctRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_COASegOptRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_COASegOptRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_COASegResRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_COASegResRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_COASegValuesListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_COASegValuesListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_COASegValuesRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_COASegValuesRow] = obj["value"]
      pass

class Erp_Tablesets_COASegAcctRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.COACode:str = obj["COACode"]
      """  Chart of Account ID  """  
      self.SegmentNbr:int = obj["SegmentNbr"]
      """  System generated number from 1 through 20.  """  
      self.SegmentCode:str = obj["SegmentCode"]
      """  Segment value used to construct the GL Account.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  Unique code identifying the currency.  Only those values defined in the CurrencyMaster are allowed.  """  
      self.Allowed:bool = obj["Allowed"]
      """  Indicates the currency can be used as a transactional currency.  """  
      self.Revalue:int = obj["Revalue"]
      """   Indicates if the transaction currency amount can be revalued.  Valid values are:
0 - no revalulation (deafult)
1 - only profits
2 - only losses
3 - both profit and losses  """  
      self.GainAccount:str = obj["GainAccount"]
      """  The natural account used for booking currency gains.  """  
      self.LossAccount:str = obj["LossAccount"]
      """  The natural account used for booking currency losses.  """  
      self.AccrualAccount:str = obj["AccrualAccount"]
      """  The natural account used as the accrual account.  """  
      self.GainSegVal1:str = obj["GainSegVal1"]
      """  GainSegVal1  """  
      self.GainSegVal2:str = obj["GainSegVal2"]
      """  GainSegVal2  """  
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
      self.GainSegVal20:str = obj["GainSegVal20"]
      """  GainSegVal20  """  
      self.LossSegVal1:str = obj["LossSegVal1"]
      """  LossSegVal1  """  
      self.LossSegVal2:str = obj["LossSegVal2"]
      """  LossSegVal2  """  
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
      self.LossSegVal20:str = obj["LossSegVal20"]
      """  LossSegVal20  """  
      self.AccrualSegVal1:str = obj["AccrualSegVal1"]
      """  AccrualSegVal1  """  
      self.AccrualSegVal2:str = obj["AccrualSegVal2"]
      """  AccrualSegVal2  """  
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
      self.AccrualSegVal20:str = obj["AccrualSegVal20"]
      """  AccrualSegVal20  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.AccrualGLDesc:str = obj["AccrualGLDesc"]
      """  Accrual GL Account description  """  
      self.GainGLDesc:str = obj["GainGLDesc"]
      """  Gain GL Account Description  """  
      self.LossGLDesc:str = obj["LossGLDesc"]
      """  Loss GL Account Description  """  
      self.BitFlag:int = obj["BitFlag"]
      self.CurrencyCurrencyID:str = obj["CurrencyCurrencyID"]
      self.CurrencyCurrDesc:str = obj["CurrencyCurrDesc"]
      self.CurrencyDocumentDesc:str = obj["CurrencyDocumentDesc"]
      self.CurrencyCurrName:str = obj["CurrencyCurrName"]
      self.CurrencyCurrSymbol:str = obj["CurrencyCurrSymbol"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_COASegOptRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.COACode:str = obj["COACode"]
      """  Chart of Account ID  """  
      self.SegmentNbr:int = obj["SegmentNbr"]
      """  System generated number from 1 through 20.  """  
      self.SegmentCode:str = obj["SegmentCode"]
      """  Segment value used to construct the GL Account.  """  
      self.SubSegmentNbr:int = obj["SubSegmentNbr"]
      """  System generated sequence number  """  
      self.ValOption:str = obj["ValOption"]
      """   Indicates if a segment is used for the natural account.  Valid values are:
M - Mandatory
O - Optional
N - Not Used  """  
      self.DefaultSegment:str = obj["DefaultSegment"]
      """  Indicates the default segment value to be used for this natural account.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.COASegmentSegmentName:str = obj["COASegmentSegmentName"]
      self.COASubSegmentSegmentName:str = obj["COASubSegmentSegmentName"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_COASegResRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.COACode:str = obj["COACode"]
      """  Chart of Account ID  """  
      self.SegmentNbr:int = obj["SegmentNbr"]
      """  System generated number from 1 through 20.  """  
      self.SegmentCode:str = obj["SegmentCode"]
      """  Segment value used to construct the GL Account.  """  
      self.RestrictID:str = obj["RestrictID"]
      """  Application DLL name  """  
      self.RestrictText:str = obj["RestrictText"]
      """  Application name text.  """  
      self.FctBlocked:bool = obj["FctBlocked"]
      """  Indicates if GL Account entry is prohibited  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_COASegValuesListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.COACode:str = obj["COACode"]
      """  Chart of Account ID  """  
      self.SegmentNbr:int = obj["SegmentNbr"]
      """  System generated number from 1 through 20.  """  
      self.SegmentCode:str = obj["SegmentCode"]
      """  Segment value used to construct the GL Account.  """  
      self.SegmentName:str = obj["SegmentName"]
      """  Name of Segment Value  """  
      self.SegmentDesc:str = obj["SegmentDesc"]
      """  Segment description.  """  
      self.SegmentAbbrev:str = obj["SegmentAbbrev"]
      """  Short name of the segment value.  """  
      self.ActiveFlag:bool = obj["ActiveFlag"]
      """  Indicates if the segment is active.  Transactions cannot be posted to inactive segments.  """  
      self.EffectiveFrom:str = obj["EffectiveFrom"]
      """  Date the segment begins to be used.  It must be less than or equal to the EffectiveTo date.  """  
      self.EffectiveTo:str = obj["EffectiveTo"]
      """  Date the segment is no longer used.  It must be greater than or equal to the EffectiveFrom date, if a value was entered in that field.  """  
      self.Category:str = obj["Category"]
      """  Required for the Natrual Account (segment number 1). Identifies the account category that is used to determine other characteristics.  """  
      self.NormalBalance:str = obj["NormalBalance"]
      """  Indicates if the account is a debit or credit and is only valid for the natural account (segment 1).  Valid values are D for Debit and C for Credit.  """  
      self.DebitRateType:str = obj["DebitRateType"]
      """  Rate type used for debit balances.  """  
      self.CreditRateType:str = obj["CreditRateType"]
      """  Rate type used for credit balances  """  
      self.CurrAcct:bool = obj["CurrAcct"]
      """  Curency Account  """  
      self.RefEntityType:str = obj["RefEntityType"]
      """  Reference Entity type assigned to this COASegValue.  Only valid when the COASegment.RefEntity = "GLCOARefType".  """  
      self.Summarization:int = obj["Summarization"]
      """   0)      Summarize (default)
1)      Summarize debit and credits separately
2)      No summarization  """  
      self.MatchingEnabled:bool = obj["MatchingEnabled"]
      """  This flag determines if journal detail records with this natural account are allowed to be matched.  """  
      self.Statistical:int = obj["Statistical"]
      """   Identifies if statistical information may be entered for the natural (chart) account.
Accounts can be used only for monetary amounts, both monetary and statistical amounts or only for statistical amounts.
0 = Only used for monetary amounts.
1 = Used for both monetary and statistical amounts.
2 = Only used for statistical amounts.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.ReverseCategory:str = obj["ReverseCategory"]
      """  Identifies the account category this is used to determine characteristics when the segment value is reversed.  """  
      self.CurrencyAcctType:str = obj["CurrencyAcctType"]
      """  CurrencyAcctType  """  
      self.RevalueOpt:int = obj["RevalueOpt"]
      """  RevalueOpt  """  
      self.COSegDtlNbr:int = obj["COSegDtlNbr"]
      """  COSegDtlNbr  """  
      self.COPrintBalanceInvDtl:bool = obj["COPrintBalanceInvDtl"]
      """  COPrintBalanceInvDtl  """  
      self.ChartInUse:bool = obj["ChartInUse"]
      """  Logical indicating if this chart has been used.  """  
      self.SegValInUse:bool = obj["SegValInUse"]
      """  Logical indicating if this segment value has been used.  """  
      self.SegWithSegOneControl:bool = obj["SegWithSegOneControl"]
      """  Logical indicating whether or not the COA has a segment defined as 'entry control' equal to natural account and controls whether or not a segment option record can be entered for a natural account value.  """  
      self.RefTypeRqd:bool = obj["RefTypeRqd"]
      """  Logical indicating if the reference type is required for this segment value  """  
      self.SegNbrName:str = obj["SegNbrName"]
      """  Segment number name from the COASegment table.  Used for display purposes in segment value searches where more than one segment number is searched at a time.  """  
      self.ReverseCategoryDescription:str = obj["ReverseCategoryDescription"]
      self.CategoryIDDescription:str = obj["CategoryIDDescription"]
      """  Text describing this category  """  
      self.CreditRateGrpDescription:str = obj["CreditRateGrpDescription"]
      """  Description  """  
      self.DebitRateGrpDescription:str = obj["DebitRateGrpDescription"]
      """  Description  """  
      self.GLCOARefTypeRefTypeDesc:str = obj["GLCOARefTypeRefTypeDesc"]
      """  Description of the Reference type  """  
      self.StatisticalDesc:str = obj["StatisticalDesc"]
      self.EffectiveRevalueOpt:int = obj["EffectiveRevalueOpt"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_COASegValuesRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.COACode:str = obj["COACode"]
      """  Chart of Account ID  """  
      self.SegmentNbr:int = obj["SegmentNbr"]
      """  System generated number from 1 through 20.  """  
      self.SegmentCode:str = obj["SegmentCode"]
      """  Segment value used to construct the GL Account.  """  
      self.SegmentName:str = obj["SegmentName"]
      """  Name of Segment Value  """  
      self.SegmentDesc:str = obj["SegmentDesc"]
      """  Segment description.  """  
      self.SegmentAbbrev:str = obj["SegmentAbbrev"]
      """  Short name of the segment value.  """  
      self.ActiveFlag:bool = obj["ActiveFlag"]
      """  Indicates if the segment is active.  Transactions cannot be posted to inactive segments.  """  
      self.EffectiveFrom:str = obj["EffectiveFrom"]
      """  Date the segment begins to be used.  It must be less than or equal to the EffectiveTo date.  """  
      self.EffectiveTo:str = obj["EffectiveTo"]
      """  Date the segment is no longer used.  It must be greater than or equal to the EffectiveFrom date, if a value was entered in that field.  """  
      self.Category:str = obj["Category"]
      """  Required for the Natrual Account (segment number 1). Identifies the account category that is used to determine other characteristics.  """  
      self.NormalBalance:str = obj["NormalBalance"]
      """  Indicates if the account is a debit or credit and is only valid for the natural account (segment 1).  Valid values are D for Debit and C for Credit.  """  
      self.DebitRateType:str = obj["DebitRateType"]
      """  Rate type used for debit balances.  """  
      self.CreditRateType:str = obj["CreditRateType"]
      """  Rate type used for credit balances  """  
      self.CurrAcct:bool = obj["CurrAcct"]
      """  Curency Account  """  
      self.RefEntityType:str = obj["RefEntityType"]
      """  Reference Entity type assigned to this COASegValue.  Only valid when the COASegment.RefEntity = "GLCOARefType".  """  
      self.Summarization:int = obj["Summarization"]
      """   0)      Summarize (default)
1)      Summarize debit and credits separately
2)      No summarization  """  
      self.MatchingEnabled:bool = obj["MatchingEnabled"]
      """  This flag determines if journal detail records with this natural account are allowed to be matched.  """  
      self.Statistical:int = obj["Statistical"]
      """   Identifies if statistical information may be entered for the natural (chart) account.
Accounts can be used only for monetary amounts, both monetary and statistical amounts or only for statistical amounts.
0 = Only used for monetary amounts.
1 = Used for both monetary and statistical amounts.
2 = Only used for statistical amounts.  """  
      self.StatUOMCode:str = obj["StatUOMCode"]
      """  StatUOMCode  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.ReverseCategory:str = obj["ReverseCategory"]
      """  Identifies the account category this is used to determine characteristics when the segment value is reversed.  """  
      self.ExtAnalysisCode:str = obj["ExtAnalysisCode"]
      """  External financial analysis code linked to the natural account.  """  
      self.CurrencyAcctType:str = obj["CurrencyAcctType"]
      """  CurrencyAcctType  """  
      self.RevalueOpt:int = obj["RevalueOpt"]
      """  RevalueOpt  """  
      self.GLGainAcctContext:str = obj["GLGainAcctContext"]
      """  GLGainAcctContext  """  
      self.GLLossAcctContext:str = obj["GLLossAcctContext"]
      """  GLLossAcctContext  """  
      self.GainAccount:str = obj["GainAccount"]
      """  GainAccount  """  
      self.LossAccount:str = obj["LossAccount"]
      """  LossAccount  """  
      self.AccrualAccount:str = obj["AccrualAccount"]
      """  AccrualAccount  """  
      self.GainSegVal1:str = obj["GainSegVal1"]
      """  GainSegVal1  """  
      self.GainSegVal2:str = obj["GainSegVal2"]
      """  GainSegVal2  """  
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
      self.GainSegVal20:str = obj["GainSegVal20"]
      """  GainSegVal20  """  
      self.LossSegVal1:str = obj["LossSegVal1"]
      """  LossSegVal1  """  
      self.LossSegVal2:str = obj["LossSegVal2"]
      """  LossSegVal2  """  
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
      self.LossSegVal20:str = obj["LossSegVal20"]
      """  LossSegVal20  """  
      self.AccrualSegVal1:str = obj["AccrualSegVal1"]
      """  AccrualSegVal1  """  
      self.AccrualSegVal2:str = obj["AccrualSegVal2"]
      """  AccrualSegVal2  """  
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
      self.AccrualSegVal20:str = obj["AccrualSegVal20"]
      """  AccrualSegVal20  """  
      self.COSegDtlNbr:int = obj["COSegDtlNbr"]
      """  COSegDtlNbr  """  
      self.COPrintBalanceInvDtl:bool = obj["COPrintBalanceInvDtl"]
      """  COPrintBalanceInvDtl  """  
      self.BENAEID:str = obj["BENAEID"]
      """  Non-Admissible Expense Code (CSF Belgium)  """  
      self.Mapped:bool = obj["Mapped"]
      """  Mapped  """  
      self.ReportCategory:str = obj["ReportCategory"]
      """  One of the UD codes having a CodeTypeID equal to GLRepCat. Or, if GLRepCat does not exist, then it may be free text.  """  
      self.ReverseReportCategory:str = obj["ReverseReportCategory"]
      """  ReverseReportCategory  """  
      self.LinkedPlant:str = obj["LinkedPlant"]
      """  LinkedPlant  """  
      self.AccrualAcctDesc:str = obj["AccrualAcctDesc"]
      """  Accrual Account Description  """  
      self.GainAcctDesc:str = obj["GainAcctDesc"]
      """  Gain Account Description  """  
      self.GlbValuesFlag:bool = obj["GlbValuesFlag"]
      self.GlobalSegValues:bool = obj["GlobalSegValues"]
      self.GlobalSegValuesLock:bool = obj["GlobalSegValuesLock"]
      self.LossAcctDesc:str = obj["LossAcctDesc"]
      """  Loss Account Description  """  
      self.RebuildGLAccts:bool = obj["RebuildGLAccts"]
      """  Internal logical used by UI that indicates if GLAccounts exist for this COA and that the display gl account must be rebuilt  """  
      self.RefTypeRqd:bool = obj["RefTypeRqd"]
      """  Logical indicating if the reference type is required for this segment value  """  
      self.ReverseCategoryDescription:str = obj["ReverseCategoryDescription"]
      self.SegNbrName:str = obj["SegNbrName"]
      """  Segment number name from the COASegment table.  Used for display purposes in segment value searches where more than one segment number is searched at a time.  """  
      self.SegValInUse:bool = obj["SegValInUse"]
      """  Logical indicating if this segment value has been used.  """  
      self.SegWithSegOneControl:bool = obj["SegWithSegOneControl"]
      """  Logical indicating whether or not the COA has a segment defined as 'entry control' equal to natural account and controls whether or not a segment option record can be entered for a natural account value.  """  
      self.StatisticalDesc:str = obj["StatisticalDesc"]
      self.ChartInUse:bool = obj["ChartInUse"]
      """  Logical indicating if this chart has been used.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.CategoryIDDescription:str = obj["CategoryIDDescription"]
      self.COASegmentSiteSegment:bool = obj["COASegmentSiteSegment"]
      self.COASegmentSegmentName:str = obj["COASegmentSegmentName"]
      self.COSegDtlSegmentName:str = obj["COSegDtlSegmentName"]
      self.CreditRateGrpDescription:str = obj["CreditRateGrpDescription"]
      self.DebitRateGrpDescription:str = obj["DebitRateGrpDescription"]
      self.GLCOARefTypeRefTypeDesc:str = obj["GLCOARefTypeRefTypeDesc"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      self.UD_SysRevID:str = obj["UD_SysRevID"]
      self.BudgetSegCode_c:str = obj["BudgetSegCode_c"]
      self.BudgetReportGroup_c:str = obj["BudgetReportGroup_c"]
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class COASegValueActiveFlagChanging_input:
   """ Required : 
   proposedActiveFlag
   ds
   """  
   def __init__(self, obj):
      self.proposedActiveFlag:bool = obj["proposedActiveFlag"]
      """  Proposed ActiveFlag value  """  
      self.ds:list[Erp_Tablesets_COASegValuesTableset] = obj["ds"]
      pass

class COASegValueActiveFlagChanging_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_COASegValuesTableset] = obj["ds"]
      self.msgInActive:str = obj["parameters"]
      self.msgActive:str = obj["parameters"]
      pass

      """  output parameters  """  

class ChangeAccountContext_input:
   """ Required : 
   context
   """  
   def __init__(self, obj):
      self.context:str = obj["context"]
      pass

class ChangeAccountContext_output:
   def __init__(self, obj):
      pass

class ChangeActive_input:
   """ Required : 
   active
   ds
   """  
   def __init__(self, obj):
      self.active:bool = obj["active"]
      self.ds:list[Erp_Tablesets_COASegValuesTableset] = obj["ds"]
      pass

class ChangeActive_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_COASegValuesTableset] = obj["ds"]
      self.msgInActive:str = obj["parameters"]
      self.msgActive:str = obj["parameters"]
      pass

      """  output parameters  """  

class ChangeAllowed_input:
   """ Required : 
   proposedAllowed
   ipCOACode
   ipSegmentNbr
   ipSegmentCode
   ipCurrencyCode
   ds
   """  
   def __init__(self, obj):
      self.proposedAllowed:bool = obj["proposedAllowed"]
      """  The proposed  Allowed value  """  
      self.ipCOACode:str = obj["ipCOACode"]
      """  The proposed  Allowed value  """  
      self.ipSegmentNbr:int = obj["ipSegmentNbr"]
      """  The proposed  Allowed value  """  
      self.ipSegmentCode:str = obj["ipSegmentCode"]
      """  The proposed  Allowed value  """  
      self.ipCurrencyCode:str = obj["ipCurrencyCode"]
      """  The proposed  Allowed value  """  
      self.ds:list[Erp_Tablesets_COASegValuesTableset] = obj["ds"]
      pass

class ChangeAllowed_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_COASegValuesTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeCategory_input:
   """ Required : 
   proposedCategory
   ds
   """  
   def __init__(self, obj):
      self.proposedCategory:str = obj["proposedCategory"]
      """  The proposed  Amount  """  
      self.ds:list[Erp_Tablesets_COASegValuesTableset] = obj["ds"]
      pass

class ChangeCategory_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_COASegValuesTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeCurrencyAccount_input:
   """ Required : 
   ipValue
   ds
   """  
   def __init__(self, obj):
      self.ipValue:str = obj["ipValue"]
      """  Currency Account flag  """  
      self.ds:list[Erp_Tablesets_COASegValuesTableset] = obj["ds"]
      pass

class ChangeCurrencyAccount_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_COASegValuesTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeLinkedPlant_input:
   """ Required : 
   linkedPlant
   ds
   """  
   def __init__(self, obj):
      self.linkedPlant:str = obj["linkedPlant"]
      self.ds:list[Erp_Tablesets_COASegValuesTableset] = obj["ds"]
      pass

class ChangeLinkedPlant_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_COASegValuesTableset] = obj["ds"]
      self.msg:str = obj["parameters"]
      self.GLmsg:str = obj["parameters"]
      pass

      """  output parameters  """  

class ChangeRateType_input:
   """ Required : 
   rateType
   isCredit
   """  
   def __init__(self, obj):
      self.rateType:str = obj["rateType"]
      self.isCredit:bool = obj["isCredit"]
      pass

class ChangeRateType_output:
   def __init__(self, obj):
      pass

class ChangeRevalueOpt_input:
   """ Required : 
   proposedRevalue
   ds
   """  
   def __init__(self, obj):
      self.proposedRevalue:int = obj["proposedRevalue"]
      self.ds:list[Erp_Tablesets_COASegValuesTableset] = obj["ds"]
      pass

class ChangeRevalueOpt_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_COASegValuesTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeSegvalue_input:
   """ Required : 
   ipValue
   ds
   """  
   def __init__(self, obj):
      self.ipValue:str = obj["ipValue"]
      """  The proposed segment value  """  
      self.ds:list[Erp_Tablesets_COASegValuesTableset] = obj["ds"]
      pass

class ChangeSegvalue_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_COASegValuesTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeSiteSegmentCode_input:
   """ Required : 
   linkedPlant
   segmentCode
   ds
   """  
   def __init__(self, obj):
      self.linkedPlant:str = obj["linkedPlant"]
      self.segmentCode:str = obj["segmentCode"]
      self.ds:list[Erp_Tablesets_SiteSegmentSetupTableset] = obj["ds"]
      pass

class ChangeSiteSegmentCode_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_SiteSegmentSetupTableset] = obj["ds"]
      self.msg:str = obj["parameters"]
      self.GLmsg:str = obj["parameters"]
      pass

      """  output parameters  """  

class ChangeStatUOMCode_input:
   """ Required : 
   statUOMCode
   ds
   """  
   def __init__(self, obj):
      self.statUOMCode:str = obj["statUOMCode"]
      self.ds:list[Erp_Tablesets_COASegValuesTableset] = obj["ds"]
      pass

class ChangeStatUOMCode_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_COASegValuesTableset] = obj["ds"]
      self.msg:str = obj["parameters"]
      pass

      """  output parameters  """  

class ChangeStatisticalOnly_input:
   """ Required : 
   segmentCode
   coaCode
   """  
   def __init__(self, obj):
      self.segmentCode:str = obj["segmentCode"]
      self.coaCode:str = obj["coaCode"]
      pass

class ChangeStatisticalOnly_output:
   def __init__(self, obj):
      pass

class ChangeStatistical_input:
   """ Required : 
   statistical
   ds
   """  
   def __init__(self, obj):
      self.statistical:int = obj["statistical"]
      self.ds:list[Erp_Tablesets_COASegValuesTableset] = obj["ds"]
      pass

class ChangeStatistical_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_COASegValuesTableset] = obj["ds"]
      self.msg:str = obj["parameters"]
      pass

      """  output parameters  """  

class CheckCOASeparatorInSegmentValue_input:
   """ Required : 
   coaCode
   segmentCode
   """  
   def __init__(self, obj):
      self.coaCode:str = obj["coaCode"]
      """  COA Code  """  
      self.segmentCode:str = obj["segmentCode"]
      """  Segment Code  """  
      pass

class CheckCOASeparatorInSegmentValue_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.warnMessage:str = obj["parameters"]
      pass

      """  output parameters  """  

class CheckForDupSegOpt_input:
   """ Required : 
   ipCOACode
   ipSubSegmentNbr
   ipSegmentCode
   """  
   def __init__(self, obj):
      self.ipCOACode:str = obj["ipCOACode"]
      self.ipSubSegmentNbr:int = obj["ipSubSegmentNbr"]
      self.ipSegmentCode:str = obj["ipSegmentCode"]
      pass

class CheckForDupSegOpt_output:
   def __init__(self, obj):
      pass

class ChgStatUOMCode_input:
   """ Required : 
   statUOMCode
   """  
   def __init__(self, obj):
      self.statUOMCode:str = obj["statUOMCode"]
      """  statUOMCode  """  
      pass

class ChgStatUOMCode_output:
   def __init__(self, obj):
      pass

class ComboValues_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.opCOACode:str = obj["parameters"]
      self.opDescription:str = obj["parameters"]
      self.opSegmentNbr:int = obj["parameters"]
      self.opSegmentName:str = obj["parameters"]
      self.opGlobalCOA:bool = obj["opGlobalCOA"]
      self.opGlobalSegment:bool = obj["opGlobalSegment"]
      pass

      """  output parameters  """  

class DefaultBookID_input:
   """ Required : 
   coaCode
   """  
   def __init__(self, obj):
      self.coaCode:str = obj["coaCode"]
      pass

class DefaultBookID_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

class DefaultsOnAddSegAcct_input:
   """ Required : 
   ipGLAccount
   ipAccountDescField
   ds
   """  
   def __init__(self, obj):
      self.ipGLAccount:str = obj["ipGLAccount"]
      """  GL Account being added  """  
      self.ipAccountDescField:str = obj["ipAccountDescField"]
      """  GL Account description field being updated  """  
      self.ds:list[Erp_Tablesets_COASegValuesTableset] = obj["ds"]
      pass

class DefaultsOnAddSegAcct_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_COASegValuesTableset] = obj["ds"]
      pass

      """  output parameters  """  

class DefaultsOnAdd_input:
   """ Required : 
   ipGLAccount
   ipAccountField
   ds
   """  
   def __init__(self, obj):
      self.ipGLAccount:str = obj["ipGLAccount"]
      """  GL Account being added  """  
      self.ipAccountField:str = obj["ipAccountField"]
      """  GL Account description field being updated  """  
      self.ds:list[Erp_Tablesets_COASegValuesTableset] = obj["ds"]
      pass

class DefaultsOnAdd_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_COASegValuesTableset] = obj["ds"]
      pass

      """  output parameters  """  

class DeleteByID_input:
   """ Required : 
   coACode
   segmentNbr
   segmentCode
   """  
   def __init__(self, obj):
      self.coACode:str = obj["coACode"]
      self.segmentNbr:int = obj["segmentNbr"]
      self.segmentCode:str = obj["segmentCode"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class DeleteTransactionCurrencies_input:
   """ Required : 
   ipCOACode
   ipSegmentNbr
   ipSegmentCode
   ds
   """  
   def __init__(self, obj):
      self.ipCOACode:str = obj["ipCOACode"]
      self.ipSegmentNbr:int = obj["ipSegmentNbr"]
      self.ipSegmentCode:str = obj["ipSegmentCode"]
      self.ds:list[Erp_Tablesets_COASegValuesTableset] = obj["ds"]
      pass

class DeleteTransactionCurrencies_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_COASegValuesTableset] = obj["ds"]
      pass

      """  output parameters  """  

class Erp_Tablesets_COASegAcctRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.COACode:str = obj["COACode"]
      """  Chart of Account ID  """  
      self.SegmentNbr:int = obj["SegmentNbr"]
      """  System generated number from 1 through 20.  """  
      self.SegmentCode:str = obj["SegmentCode"]
      """  Segment value used to construct the GL Account.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  Unique code identifying the currency.  Only those values defined in the CurrencyMaster are allowed.  """  
      self.Allowed:bool = obj["Allowed"]
      """  Indicates the currency can be used as a transactional currency.  """  
      self.Revalue:int = obj["Revalue"]
      """   Indicates if the transaction currency amount can be revalued.  Valid values are:
0 - no revalulation (deafult)
1 - only profits
2 - only losses
3 - both profit and losses  """  
      self.GainAccount:str = obj["GainAccount"]
      """  The natural account used for booking currency gains.  """  
      self.LossAccount:str = obj["LossAccount"]
      """  The natural account used for booking currency losses.  """  
      self.AccrualAccount:str = obj["AccrualAccount"]
      """  The natural account used as the accrual account.  """  
      self.GainSegVal1:str = obj["GainSegVal1"]
      """  GainSegVal1  """  
      self.GainSegVal2:str = obj["GainSegVal2"]
      """  GainSegVal2  """  
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
      self.GainSegVal20:str = obj["GainSegVal20"]
      """  GainSegVal20  """  
      self.LossSegVal1:str = obj["LossSegVal1"]
      """  LossSegVal1  """  
      self.LossSegVal2:str = obj["LossSegVal2"]
      """  LossSegVal2  """  
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
      self.LossSegVal20:str = obj["LossSegVal20"]
      """  LossSegVal20  """  
      self.AccrualSegVal1:str = obj["AccrualSegVal1"]
      """  AccrualSegVal1  """  
      self.AccrualSegVal2:str = obj["AccrualSegVal2"]
      """  AccrualSegVal2  """  
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
      self.AccrualSegVal20:str = obj["AccrualSegVal20"]
      """  AccrualSegVal20  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.AccrualGLDesc:str = obj["AccrualGLDesc"]
      """  Accrual GL Account description  """  
      self.GainGLDesc:str = obj["GainGLDesc"]
      """  Gain GL Account Description  """  
      self.LossGLDesc:str = obj["LossGLDesc"]
      """  Loss GL Account Description  """  
      self.BitFlag:int = obj["BitFlag"]
      self.CurrencyCurrencyID:str = obj["CurrencyCurrencyID"]
      self.CurrencyCurrDesc:str = obj["CurrencyCurrDesc"]
      self.CurrencyDocumentDesc:str = obj["CurrencyDocumentDesc"]
      self.CurrencyCurrName:str = obj["CurrencyCurrName"]
      self.CurrencyCurrSymbol:str = obj["CurrencyCurrSymbol"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_COASegOptRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.COACode:str = obj["COACode"]
      """  Chart of Account ID  """  
      self.SegmentNbr:int = obj["SegmentNbr"]
      """  System generated number from 1 through 20.  """  
      self.SegmentCode:str = obj["SegmentCode"]
      """  Segment value used to construct the GL Account.  """  
      self.SubSegmentNbr:int = obj["SubSegmentNbr"]
      """  System generated sequence number  """  
      self.ValOption:str = obj["ValOption"]
      """   Indicates if a segment is used for the natural account.  Valid values are:
M - Mandatory
O - Optional
N - Not Used  """  
      self.DefaultSegment:str = obj["DefaultSegment"]
      """  Indicates the default segment value to be used for this natural account.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.COASegmentSegmentName:str = obj["COASegmentSegmentName"]
      self.COASubSegmentSegmentName:str = obj["COASubSegmentSegmentName"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_COASegResRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.COACode:str = obj["COACode"]
      """  Chart of Account ID  """  
      self.SegmentNbr:int = obj["SegmentNbr"]
      """  System generated number from 1 through 20.  """  
      self.SegmentCode:str = obj["SegmentCode"]
      """  Segment value used to construct the GL Account.  """  
      self.RestrictID:str = obj["RestrictID"]
      """  Application DLL name  """  
      self.RestrictText:str = obj["RestrictText"]
      """  Application name text.  """  
      self.FctBlocked:bool = obj["FctBlocked"]
      """  Indicates if GL Account entry is prohibited  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_COASegValuesListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.COACode:str = obj["COACode"]
      """  Chart of Account ID  """  
      self.SegmentNbr:int = obj["SegmentNbr"]
      """  System generated number from 1 through 20.  """  
      self.SegmentCode:str = obj["SegmentCode"]
      """  Segment value used to construct the GL Account.  """  
      self.SegmentName:str = obj["SegmentName"]
      """  Name of Segment Value  """  
      self.SegmentDesc:str = obj["SegmentDesc"]
      """  Segment description.  """  
      self.SegmentAbbrev:str = obj["SegmentAbbrev"]
      """  Short name of the segment value.  """  
      self.ActiveFlag:bool = obj["ActiveFlag"]
      """  Indicates if the segment is active.  Transactions cannot be posted to inactive segments.  """  
      self.EffectiveFrom:str = obj["EffectiveFrom"]
      """  Date the segment begins to be used.  It must be less than or equal to the EffectiveTo date.  """  
      self.EffectiveTo:str = obj["EffectiveTo"]
      """  Date the segment is no longer used.  It must be greater than or equal to the EffectiveFrom date, if a value was entered in that field.  """  
      self.Category:str = obj["Category"]
      """  Required for the Natrual Account (segment number 1). Identifies the account category that is used to determine other characteristics.  """  
      self.NormalBalance:str = obj["NormalBalance"]
      """  Indicates if the account is a debit or credit and is only valid for the natural account (segment 1).  Valid values are D for Debit and C for Credit.  """  
      self.DebitRateType:str = obj["DebitRateType"]
      """  Rate type used for debit balances.  """  
      self.CreditRateType:str = obj["CreditRateType"]
      """  Rate type used for credit balances  """  
      self.CurrAcct:bool = obj["CurrAcct"]
      """  Curency Account  """  
      self.RefEntityType:str = obj["RefEntityType"]
      """  Reference Entity type assigned to this COASegValue.  Only valid when the COASegment.RefEntity = "GLCOARefType".  """  
      self.Summarization:int = obj["Summarization"]
      """   0)      Summarize (default)
1)      Summarize debit and credits separately
2)      No summarization  """  
      self.MatchingEnabled:bool = obj["MatchingEnabled"]
      """  This flag determines if journal detail records with this natural account are allowed to be matched.  """  
      self.Statistical:int = obj["Statistical"]
      """   Identifies if statistical information may be entered for the natural (chart) account.
Accounts can be used only for monetary amounts, both monetary and statistical amounts or only for statistical amounts.
0 = Only used for monetary amounts.
1 = Used for both monetary and statistical amounts.
2 = Only used for statistical amounts.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.ReverseCategory:str = obj["ReverseCategory"]
      """  Identifies the account category this is used to determine characteristics when the segment value is reversed.  """  
      self.CurrencyAcctType:str = obj["CurrencyAcctType"]
      """  CurrencyAcctType  """  
      self.RevalueOpt:int = obj["RevalueOpt"]
      """  RevalueOpt  """  
      self.COSegDtlNbr:int = obj["COSegDtlNbr"]
      """  COSegDtlNbr  """  
      self.COPrintBalanceInvDtl:bool = obj["COPrintBalanceInvDtl"]
      """  COPrintBalanceInvDtl  """  
      self.ChartInUse:bool = obj["ChartInUse"]
      """  Logical indicating if this chart has been used.  """  
      self.SegValInUse:bool = obj["SegValInUse"]
      """  Logical indicating if this segment value has been used.  """  
      self.SegWithSegOneControl:bool = obj["SegWithSegOneControl"]
      """  Logical indicating whether or not the COA has a segment defined as 'entry control' equal to natural account and controls whether or not a segment option record can be entered for a natural account value.  """  
      self.RefTypeRqd:bool = obj["RefTypeRqd"]
      """  Logical indicating if the reference type is required for this segment value  """  
      self.SegNbrName:str = obj["SegNbrName"]
      """  Segment number name from the COASegment table.  Used for display purposes in segment value searches where more than one segment number is searched at a time.  """  
      self.ReverseCategoryDescription:str = obj["ReverseCategoryDescription"]
      self.CategoryIDDescription:str = obj["CategoryIDDescription"]
      """  Text describing this category  """  
      self.CreditRateGrpDescription:str = obj["CreditRateGrpDescription"]
      """  Description  """  
      self.DebitRateGrpDescription:str = obj["DebitRateGrpDescription"]
      """  Description  """  
      self.GLCOARefTypeRefTypeDesc:str = obj["GLCOARefTypeRefTypeDesc"]
      """  Description of the Reference type  """  
      self.StatisticalDesc:str = obj["StatisticalDesc"]
      self.EffectiveRevalueOpt:int = obj["EffectiveRevalueOpt"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_COASegValuesListTableset:
   def __init__(self, obj):
      self.COASegValuesList:list[Erp_Tablesets_COASegValuesListRow] = obj["COASegValuesList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_COASegValuesRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.COACode:str = obj["COACode"]
      """  Chart of Account ID  """  
      self.SegmentNbr:int = obj["SegmentNbr"]
      """  System generated number from 1 through 20.  """  
      self.SegmentCode:str = obj["SegmentCode"]
      """  Segment value used to construct the GL Account.  """  
      self.SegmentName:str = obj["SegmentName"]
      """  Name of Segment Value  """  
      self.SegmentDesc:str = obj["SegmentDesc"]
      """  Segment description.  """  
      self.SegmentAbbrev:str = obj["SegmentAbbrev"]
      """  Short name of the segment value.  """  
      self.ActiveFlag:bool = obj["ActiveFlag"]
      """  Indicates if the segment is active.  Transactions cannot be posted to inactive segments.  """  
      self.EffectiveFrom:str = obj["EffectiveFrom"]
      """  Date the segment begins to be used.  It must be less than or equal to the EffectiveTo date.  """  
      self.EffectiveTo:str = obj["EffectiveTo"]
      """  Date the segment is no longer used.  It must be greater than or equal to the EffectiveFrom date, if a value was entered in that field.  """  
      self.Category:str = obj["Category"]
      """  Required for the Natrual Account (segment number 1). Identifies the account category that is used to determine other characteristics.  """  
      self.NormalBalance:str = obj["NormalBalance"]
      """  Indicates if the account is a debit or credit and is only valid for the natural account (segment 1).  Valid values are D for Debit and C for Credit.  """  
      self.DebitRateType:str = obj["DebitRateType"]
      """  Rate type used for debit balances.  """  
      self.CreditRateType:str = obj["CreditRateType"]
      """  Rate type used for credit balances  """  
      self.CurrAcct:bool = obj["CurrAcct"]
      """  Curency Account  """  
      self.RefEntityType:str = obj["RefEntityType"]
      """  Reference Entity type assigned to this COASegValue.  Only valid when the COASegment.RefEntity = "GLCOARefType".  """  
      self.Summarization:int = obj["Summarization"]
      """   0)      Summarize (default)
1)      Summarize debit and credits separately
2)      No summarization  """  
      self.MatchingEnabled:bool = obj["MatchingEnabled"]
      """  This flag determines if journal detail records with this natural account are allowed to be matched.  """  
      self.Statistical:int = obj["Statistical"]
      """   Identifies if statistical information may be entered for the natural (chart) account.
Accounts can be used only for monetary amounts, both monetary and statistical amounts or only for statistical amounts.
0 = Only used for monetary amounts.
1 = Used for both monetary and statistical amounts.
2 = Only used for statistical amounts.  """  
      self.StatUOMCode:str = obj["StatUOMCode"]
      """  StatUOMCode  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.ReverseCategory:str = obj["ReverseCategory"]
      """  Identifies the account category this is used to determine characteristics when the segment value is reversed.  """  
      self.ExtAnalysisCode:str = obj["ExtAnalysisCode"]
      """  External financial analysis code linked to the natural account.  """  
      self.CurrencyAcctType:str = obj["CurrencyAcctType"]
      """  CurrencyAcctType  """  
      self.RevalueOpt:int = obj["RevalueOpt"]
      """  RevalueOpt  """  
      self.GLGainAcctContext:str = obj["GLGainAcctContext"]
      """  GLGainAcctContext  """  
      self.GLLossAcctContext:str = obj["GLLossAcctContext"]
      """  GLLossAcctContext  """  
      self.GainAccount:str = obj["GainAccount"]
      """  GainAccount  """  
      self.LossAccount:str = obj["LossAccount"]
      """  LossAccount  """  
      self.AccrualAccount:str = obj["AccrualAccount"]
      """  AccrualAccount  """  
      self.GainSegVal1:str = obj["GainSegVal1"]
      """  GainSegVal1  """  
      self.GainSegVal2:str = obj["GainSegVal2"]
      """  GainSegVal2  """  
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
      self.GainSegVal20:str = obj["GainSegVal20"]
      """  GainSegVal20  """  
      self.LossSegVal1:str = obj["LossSegVal1"]
      """  LossSegVal1  """  
      self.LossSegVal2:str = obj["LossSegVal2"]
      """  LossSegVal2  """  
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
      self.LossSegVal20:str = obj["LossSegVal20"]
      """  LossSegVal20  """  
      self.AccrualSegVal1:str = obj["AccrualSegVal1"]
      """  AccrualSegVal1  """  
      self.AccrualSegVal2:str = obj["AccrualSegVal2"]
      """  AccrualSegVal2  """  
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
      self.AccrualSegVal20:str = obj["AccrualSegVal20"]
      """  AccrualSegVal20  """  
      self.COSegDtlNbr:int = obj["COSegDtlNbr"]
      """  COSegDtlNbr  """  
      self.COPrintBalanceInvDtl:bool = obj["COPrintBalanceInvDtl"]
      """  COPrintBalanceInvDtl  """  
      self.BENAEID:str = obj["BENAEID"]
      """  Non-Admissible Expense Code (CSF Belgium)  """  
      self.Mapped:bool = obj["Mapped"]
      """  Mapped  """  
      self.ReportCategory:str = obj["ReportCategory"]
      """  One of the UD codes having a CodeTypeID equal to GLRepCat. Or, if GLRepCat does not exist, then it may be free text.  """  
      self.ReverseReportCategory:str = obj["ReverseReportCategory"]
      """  ReverseReportCategory  """  
      self.LinkedPlant:str = obj["LinkedPlant"]
      """  LinkedPlant  """  
      self.AccrualAcctDesc:str = obj["AccrualAcctDesc"]
      """  Accrual Account Description  """  
      self.GainAcctDesc:str = obj["GainAcctDesc"]
      """  Gain Account Description  """  
      self.GlbValuesFlag:bool = obj["GlbValuesFlag"]
      self.GlobalSegValues:bool = obj["GlobalSegValues"]
      self.GlobalSegValuesLock:bool = obj["GlobalSegValuesLock"]
      self.LossAcctDesc:str = obj["LossAcctDesc"]
      """  Loss Account Description  """  
      self.RebuildGLAccts:bool = obj["RebuildGLAccts"]
      """  Internal logical used by UI that indicates if GLAccounts exist for this COA and that the display gl account must be rebuilt  """  
      self.RefTypeRqd:bool = obj["RefTypeRqd"]
      """  Logical indicating if the reference type is required for this segment value  """  
      self.ReverseCategoryDescription:str = obj["ReverseCategoryDescription"]
      self.SegNbrName:str = obj["SegNbrName"]
      """  Segment number name from the COASegment table.  Used for display purposes in segment value searches where more than one segment number is searched at a time.  """  
      self.SegValInUse:bool = obj["SegValInUse"]
      """  Logical indicating if this segment value has been used.  """  
      self.SegWithSegOneControl:bool = obj["SegWithSegOneControl"]
      """  Logical indicating whether or not the COA has a segment defined as 'entry control' equal to natural account and controls whether or not a segment option record can be entered for a natural account value.  """  
      self.StatisticalDesc:str = obj["StatisticalDesc"]
      self.ChartInUse:bool = obj["ChartInUse"]
      """  Logical indicating if this chart has been used.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.CategoryIDDescription:str = obj["CategoryIDDescription"]
      self.COASegmentSiteSegment:bool = obj["COASegmentSiteSegment"]
      self.COASegmentSegmentName:str = obj["COASegmentSegmentName"]
      self.COSegDtlSegmentName:str = obj["COSegDtlSegmentName"]
      self.CreditRateGrpDescription:str = obj["CreditRateGrpDescription"]
      self.DebitRateGrpDescription:str = obj["DebitRateGrpDescription"]
      self.GLCOARefTypeRefTypeDesc:str = obj["GLCOARefTypeRefTypeDesc"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      self.UD_SysRevID:str = obj["UD_SysRevID"]
      self.BudgetSegCode_c:str = obj["BudgetSegCode_c"]
      self.BudgetReportGroup_c:str = obj["BudgetReportGroup_c"]
      pass

class Erp_Tablesets_COASegValuesTableset:
   def __init__(self, obj):
      self.COASegValues:list[Erp_Tablesets_COASegValuesRow] = obj["COASegValues"]
      self.COASegAcct:list[Erp_Tablesets_COASegAcctRow] = obj["COASegAcct"]
      self.COASegOpt:list[Erp_Tablesets_COASegOptRow] = obj["COASegOpt"]
      self.COASegRes:list[Erp_Tablesets_COASegResRow] = obj["COASegRes"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_InterSiteAccountPairRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.BookID:str = obj["BookID"]
      self.SourcePlant:str = obj["SourcePlant"]
      self.DueFromSegValue1:str = obj["DueFromSegValue1"]
      self.DueFromSegValue2:str = obj["DueFromSegValue2"]
      self.DueFromSegValue3:str = obj["DueFromSegValue3"]
      self.DueFromSegValue4:str = obj["DueFromSegValue4"]
      self.DueFromSegValue5:str = obj["DueFromSegValue5"]
      self.DueFromSegValue6:str = obj["DueFromSegValue6"]
      self.DueFromSegValue7:str = obj["DueFromSegValue7"]
      self.DueFromSegValue8:str = obj["DueFromSegValue8"]
      self.DueFromSegValue9:str = obj["DueFromSegValue9"]
      self.DueFromSegValue10:str = obj["DueFromSegValue10"]
      self.DueFromSegValue11:str = obj["DueFromSegValue11"]
      self.DueFromSegValue12:str = obj["DueFromSegValue12"]
      self.DueFromSegValue13:str = obj["DueFromSegValue13"]
      self.DueFromSegValue14:str = obj["DueFromSegValue14"]
      self.DueFromSegValue15:str = obj["DueFromSegValue15"]
      self.DueFromSegValue16:str = obj["DueFromSegValue16"]
      self.DueFromSegValue17:str = obj["DueFromSegValue17"]
      self.DueFromSegValue18:str = obj["DueFromSegValue18"]
      self.DueFromSegValue19:str = obj["DueFromSegValue19"]
      self.DueFromSegValue20:str = obj["DueFromSegValue20"]
      self.TargetPlant:str = obj["TargetPlant"]
      self.DueToSegValue1:str = obj["DueToSegValue1"]
      self.DueToSegValue2:str = obj["DueToSegValue2"]
      self.DueToSegValue3:str = obj["DueToSegValue3"]
      self.DueToSegValue4:str = obj["DueToSegValue4"]
      self.DueToSegValue5:str = obj["DueToSegValue5"]
      self.DueToSegValue6:str = obj["DueToSegValue6"]
      self.DueToSegValue7:str = obj["DueToSegValue7"]
      self.DueToSegValue8:str = obj["DueToSegValue8"]
      self.DueToSegValue9:str = obj["DueToSegValue9"]
      self.DueToSegValue10:str = obj["DueToSegValue10"]
      self.DueToSegValue11:str = obj["DueToSegValue11"]
      self.DueToSegValue12:str = obj["DueToSegValue12"]
      self.DueToSegValue13:str = obj["DueToSegValue13"]
      self.DueToSegValue14:str = obj["DueToSegValue14"]
      self.DueToSegValue15:str = obj["DueToSegValue15"]
      self.DueToSegValue16:str = obj["DueToSegValue16"]
      self.DueToSegValue17:str = obj["DueToSegValue17"]
      self.DueToSegValue18:str = obj["DueToSegValue18"]
      self.DueToSegValue19:str = obj["DueToSegValue19"]
      self.DueToSegValue20:str = obj["DueToSegValue20"]
      self.COACode:str = obj["COACode"]
      self.BookDescription:str = obj["BookDescription"]
      self.SourcePlantName:str = obj["SourcePlantName"]
      self.TargetPlantName:str = obj["TargetPlantName"]
      self.InvalidDueFromAccount:bool = obj["InvalidDueFromAccount"]
      """  Indicates if the due from account is invalid  """  
      self.DueFromGLAccount:str = obj["DueFromGLAccount"]
      self.DueFromGLAccountDesc:str = obj["DueFromGLAccountDesc"]
      self.DueToGLAccount:str = obj["DueToGLAccount"]
      self.InvalidDueToAccount:bool = obj["InvalidDueToAccount"]
      """  Indicates if the due to account is invalid  """  
      self.DueToGLAccountDesc:str = obj["DueToGLAccountDesc"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_SiteSegmentSetupRow:
   def __init__(self, obj):
      self.COACode:str = obj["COACode"]
      """  Chart of Account ID  """  
      self.GLControlCode:str = obj["GLControlCode"]
      """  GL Control Identifier.  """  
      self.LinkedPlant:str = obj["LinkedPlant"]
      """  Linked Site  """  
      self.SegmentAbbrev:str = obj["SegmentAbbrev"]
      """  Short name of the segment value.  """  
      self.SegmentCode:str = obj["SegmentCode"]
      self.SegmentName:str = obj["SegmentName"]
      """  Name of Segment Value  """  
      self.SegmentDesc:str = obj["SegmentDesc"]
      """  Segment Description  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_SiteSegmentSetupTableset:
   def __init__(self, obj):
      self.InterSiteAccountPair:list[Erp_Tablesets_InterSiteAccountPairRow] = obj["InterSiteAccountPair"]
      self.SiteSegmentSetup:list[Erp_Tablesets_SiteSegmentSetupRow] = obj["SiteSegmentSetup"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_UpdExtCOASegValuesTableset:
   def __init__(self, obj):
      self.COASegValues:list[Erp_Tablesets_COASegValuesRow] = obj["COASegValues"]
      self.COASegAcct:list[Erp_Tablesets_COASegAcctRow] = obj["COASegAcct"]
      self.COASegOpt:list[Erp_Tablesets_COASegOptRow] = obj["COASegOpt"]
      self.COASegRes:list[Erp_Tablesets_COASegResRow] = obj["COASegRes"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GenerateSiteSegmentSetupData_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_SiteSegmentSetupTableset] = obj["ds"]
      pass

class GenerateSiteSegmentSetupData_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_SiteSegmentSetupTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetByID_input:
   """ Required : 
   coACode
   segmentNbr
   segmentCode
   """  
   def __init__(self, obj):
      self.coACode:str = obj["coACode"]
      self.segmentNbr:int = obj["segmentNbr"]
      self.segmentCode:str = obj["segmentCode"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_COASegValuesTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_COASegValuesTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_COASegValuesTableset] = obj["returnObj"]
      pass

class GetCOASegmentGlobalFields_input:
   """ Required : 
   COACode
   SegmentNbr
   GlobalLock
   """  
   def __init__(self, obj):
      self.COACode:str = obj["COACode"]
      self.SegmentNbr:int = obj["SegmentNbr"]
      self.GlobalLock:bool = obj["GlobalLock"]
      pass

class GetCOASegmentGlobalFields_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

class GetInterSiteAccountPairs_input:
   """ Required : 
   coaCode
   ds
   """  
   def __init__(self, obj):
      self.coaCode:str = obj["coaCode"]
      """  COA Code  """  
      self.ds:list[Erp_Tablesets_SiteSegmentSetupTableset] = obj["ds"]
      pass

class GetInterSiteAccountPairs_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_SiteSegmentSetupTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetListCBOnly_input:
   """ Required : 
   WhereClause
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.WhereClause:str = obj["WhereClause"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetListCBOnly_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_COASegValuesListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
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
      self.returnObj:list[Erp_Tablesets_COASegValuesListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewCOASegAcct_input:
   """ Required : 
   ds
   coACode
   segmentNbr
   segmentCode
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_COASegValuesTableset] = obj["ds"]
      self.coACode:str = obj["coACode"]
      self.segmentNbr:int = obj["segmentNbr"]
      self.segmentCode:str = obj["segmentCode"]
      pass

class GetNewCOASegAcct_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_COASegValuesTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewCOASegOpt_input:
   """ Required : 
   ds
   coACode
   segmentNbr
   segmentCode
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_COASegValuesTableset] = obj["ds"]
      self.coACode:str = obj["coACode"]
      self.segmentNbr:int = obj["segmentNbr"]
      self.segmentCode:str = obj["segmentCode"]
      pass

class GetNewCOASegOpt_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_COASegValuesTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewCOASegRes_input:
   """ Required : 
   ds
   coACode
   segmentNbr
   segmentCode
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_COASegValuesTableset] = obj["ds"]
      self.coACode:str = obj["coACode"]
      self.segmentNbr:int = obj["segmentNbr"]
      self.segmentCode:str = obj["segmentCode"]
      pass

class GetNewCOASegRes_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_COASegValuesTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewCOASegValues_input:
   """ Required : 
   ds
   coACode
   segmentNbr
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_COASegValuesTableset] = obj["ds"]
      self.coACode:str = obj["coACode"]
      self.segmentNbr:int = obj["segmentNbr"]
      pass

class GetNewCOASegValues_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_COASegValuesTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseCOASegValues
   whereClauseCOASegAcct
   whereClauseCOASegOpt
   whereClauseCOASegRes
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseCOASegValues:str = obj["whereClauseCOASegValues"]
      self.whereClauseCOASegAcct:str = obj["whereClauseCOASegAcct"]
      self.whereClauseCOASegOpt:str = obj["whereClauseCOASegOpt"]
      self.whereClauseCOASegRes:str = obj["whereClauseCOASegRes"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_COASegValuesTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetSiteSegmentSetupData_input:
   """ Required : 
   coaCode
   ds
   """  
   def __init__(self, obj):
      self.coaCode:str = obj["coaCode"]
      self.ds:list[Erp_Tablesets_SiteSegmentSetupTableset] = obj["ds"]
      pass

class GetSiteSegmentSetupData_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_SiteSegmentSetupTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetSiteSetting_input:
   """ Required : 
   COACode
   """  
   def __init__(self, obj):
      self.COACode:str = obj["COACode"]
      pass

class GetSiteSetting_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.showSiteWizard:bool = obj["showSiteWizard"]
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

class IntersiteAccountPairsApply_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_SiteSegmentSetupTableset] = obj["ds"]
      pass

class IntersiteAccountPairsApply_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_SiteSegmentSetupTableset] = obj["ds"]
      self.invalidAccountMessage:str = obj["parameters"]
      self.incompletePairMessage:str = obj["parameters"]
      pass

      """  output parameters  """  

class IsStatOnlySegment_input:
   """ Required : 
   ipCompany
   ipCOACode
   ipSegmentCode
   """  
   def __init__(self, obj):
      self.ipCompany:str = obj["ipCompany"]
      self.ipCOACode:str = obj["ipCOACode"]
      self.ipSegmentCode:str = obj["ipSegmentCode"]
      pass

class IsStatOnlySegment_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      pass

class RemoveSiteSegmentCodeDuplicate_input:
   """ Required : 
   linkedPlant
   segmentCode
   ds
   """  
   def __init__(self, obj):
      self.linkedPlant:str = obj["linkedPlant"]
      self.segmentCode:str = obj["segmentCode"]
      self.ds:list[Erp_Tablesets_SiteSegmentSetupTableset] = obj["ds"]
      pass

class RemoveSiteSegmentCodeDuplicate_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_SiteSegmentSetupTableset] = obj["ds"]
      pass

      """  output parameters  """  

class SiteSegmentChanged_input:
   """ Required : 
   plant
   ds
   """  
   def __init__(self, obj):
      self.plant:str = obj["plant"]
      self.ds:list[Erp_Tablesets_SiteSegmentSetupTableset] = obj["ds"]
      pass

class SiteSegmentChanged_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_SiteSegmentSetupTableset] = obj["ds"]
      pass

      """  output parameters  """  

class SiteSegmentSetupApply_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_SiteSegmentSetupTableset] = obj["ds"]
      pass

class SiteSegmentSetupApply_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_SiteSegmentSetupTableset] = obj["ds"]
      self.msg:str = obj["parameters"]
      pass

      """  output parameters  """  

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtCOASegValuesTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtCOASegValuesTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_COASegValuesTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_COASegValuesTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ValidateCOACodeSite_input:
   """ Required : 
   coaCode
   segNbr
   """  
   def __init__(self, obj):
      self.coaCode:str = obj["coaCode"]
      """  COA code entered  """  
      self.segNbr:str = obj["segNbr"]
      """  segNbr  """  
      pass

class ValidateCOACodeSite_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.opDescription:str = obj["parameters"]
      self.opSegmentNbr:int = obj["parameters"]
      self.opSegmentName:str = obj["parameters"]
      self.opGlobalCOA:bool = obj["opGlobalCOA"]
      self.opGlobalSegment:bool = obj["opGlobalSegment"]
      self.opSiteSegment:bool = obj["opSiteSegment"]
      pass

      """  output parameters  """  

class ValidateCOACode_input:
   """ Required : 
   coaCode
   segNbr
   """  
   def __init__(self, obj):
      self.coaCode:str = obj["coaCode"]
      """  COA code entered  """  
      self.segNbr:str = obj["segNbr"]
      """  segNbr  """  
      pass

class ValidateCOACode_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.opDescription:str = obj["parameters"]
      self.opSegmentNbr:int = obj["parameters"]
      self.opSegmentName:str = obj["parameters"]
      self.opGlobalCOA:bool = obj["opGlobalCOA"]
      self.opGlobalSegment:bool = obj["opGlobalSegment"]
      pass

      """  output parameters  """  

class ValidateCOASegment_input:
   """ Required : 
   ipCOACode
   ipSegmentNbr
   """  
   def __init__(self, obj):
      self.ipCOACode:str = obj["ipCOACode"]
      """  COA Code  """  
      self.ipSegmentNbr:int = obj["ipSegmentNbr"]
      """  Segment Number  """  
      pass

class ValidateCOASegment_output:
   def __init__(self, obj):
      pass

class ValidateCurrencyAccount_input:
   """ Required : 
   ipCOACode
   ipSegmentCode
   ipCurrencyAcct
   CurrencyAcctType
   """  
   def __init__(self, obj):
      self.ipCOACode:str = obj["ipCOACode"]
      self.ipSegmentCode:str = obj["ipSegmentCode"]
      self.ipCurrencyAcct:bool = obj["ipCurrencyAcct"]
      self.CurrencyAcctType:str = obj["CurrencyAcctType"]
      pass

class ValidateCurrencyAccount_output:
   def __init__(self, obj):
      pass

class ValidateDefaultSegment_input:
   """ Required : 
   ipCOACode
   ipSubSegmentNbr
   ipSegmentCode
   """  
   def __init__(self, obj):
      self.ipCOACode:str = obj["ipCOACode"]
      self.ipSubSegmentNbr:int = obj["ipSubSegmentNbr"]
      self.ipSegmentCode:str = obj["ipSegmentCode"]
      pass

class ValidateDefaultSegment_output:
   def __init__(self, obj):
      pass

class getBookRevOpt_input:
   """ Required : 
   pbookID
   pCOACode
   """  
   def __init__(self, obj):
      self.pbookID:str = obj["pbookID"]
      self.pCOACode:str = obj["pCOACode"]
      pass

class getBookRevOpt_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.pEffRevOpt:int = obj["parameters"]
      pass

      """  output parameters  """  

