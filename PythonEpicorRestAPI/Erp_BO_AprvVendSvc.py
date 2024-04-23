import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.AprvVendSvc
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AprvVendSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AprvVendSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_AprvVends(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get AprvVends items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_AprvVends
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.AprvVendRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AprvVendSvc/AprvVends",headers=creds) as resp:
           return await resp.json()

async def post_AprvVends(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_AprvVends
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.AprvVendRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.AprvVendRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AprvVendSvc/AprvVends", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_AprvVends_Company_VendorNum_PartNum_APVType_ClassID_OpCode_CustNum(Company, VendorNum, PartNum, APVType, ClassID, OpCode, CustNum, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the AprvVend item
   Description: Calls GetByID to retrieve the AprvVend item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_AprvVend
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param VendorNum: Desc: VendorNum   Required: True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param APVType: Desc: APVType   Required: True   Allow empty value : True
      :param ClassID: Desc: ClassID   Required: True   Allow empty value : True
      :param OpCode: Desc: OpCode   Required: True   Allow empty value : True
      :param CustNum: Desc: CustNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.AprvVendRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AprvVendSvc/AprvVends(" + Company + "," + VendorNum + "," + PartNum + "," + APVType + "," + ClassID + "," + OpCode + "," + CustNum + ")",headers=creds) as resp:
           return await resp.json()

async def patch_AprvVends_Company_VendorNum_PartNum_APVType_ClassID_OpCode_CustNum(Company, VendorNum, PartNum, APVType, ClassID, OpCode, CustNum, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update AprvVend for the service
   Description: Calls UpdateExt to update AprvVend. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_AprvVend
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param VendorNum: Desc: VendorNum   Required: True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param APVType: Desc: APVType   Required: True   Allow empty value : True
      :param ClassID: Desc: ClassID   Required: True   Allow empty value : True
      :param OpCode: Desc: OpCode   Required: True   Allow empty value : True
      :param CustNum: Desc: CustNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.AprvVendRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.AprvVendSvc/AprvVends(" + Company + "," + VendorNum + "," + PartNum + "," + APVType + "," + ClassID + "," + OpCode + "," + CustNum + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_AprvVends_Company_VendorNum_PartNum_APVType_ClassID_OpCode_CustNum(Company, VendorNum, PartNum, APVType, ClassID, OpCode, CustNum, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete AprvVend item
   Description: Call UpdateExt to delete AprvVend item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_AprvVend
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param VendorNum: Desc: VendorNum   Required: True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param APVType: Desc: APVType   Required: True   Allow empty value : True
      :param ClassID: Desc: ClassID   Required: True   Allow empty value : True
      :param OpCode: Desc: OpCode   Required: True   Allow empty value : True
      :param CustNum: Desc: CustNum   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.AprvVendSvc/AprvVends(" + Company + "," + VendorNum + "," + PartNum + "," + APVType + "," + ClassID + "," + OpCode + "," + CustNum + ")",headers=creds) as resp:
           return await resp.json()

async def get_AprvVends_Company_VendorNum_PartNum_APVType_ClassID_OpCode_CustNum_PartXRefVends(Company, VendorNum, PartNum, APVType, ClassID, OpCode, CustNum, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get PartXRefVends items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_PartXRefVends1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param VendorNum: Desc: VendorNum   Required: True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param APVType: Desc: APVType   Required: True   Allow empty value : True
      :param ClassID: Desc: ClassID   Required: True   Allow empty value : True
      :param OpCode: Desc: OpCode   Required: True   Allow empty value : True
      :param CustNum: Desc: CustNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PartXRefVendRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AprvVendSvc/AprvVends(" + Company + "," + VendorNum + "," + PartNum + "," + APVType + "," + ClassID + "," + OpCode + "," + CustNum + ")/PartXRefVends",headers=creds) as resp:
           return await resp.json()

async def get_AprvVends_Company_VendorNum_PartNum_APVType_ClassID_OpCode_CustNum_PartXRefVends_Company_PartNum_VendorNum_VendPartNum_MfgNum_MfgPartNum(Company, VendorNum, PartNum, APVType, ClassID, OpCode, CustNum, VendPartNum, MfgNum, MfgPartNum, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PartXRefVend item
   Description: Calls GetByID to retrieve the PartXRefVend item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PartXRefVend1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param VendorNum: Desc: VendorNum   Required: True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param APVType: Desc: APVType   Required: True   Allow empty value : True
      :param ClassID: Desc: ClassID   Required: True   Allow empty value : True
      :param OpCode: Desc: OpCode   Required: True   Allow empty value : True
      :param CustNum: Desc: CustNum   Required: True
      :param VendPartNum: Desc: VendPartNum   Required: True   Allow empty value : True
      :param MfgNum: Desc: MfgNum   Required: True
      :param MfgPartNum: Desc: MfgPartNum   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PartXRefVendRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AprvVendSvc/AprvVends(" + Company + "," + VendorNum + "," + PartNum + "," + APVType + "," + ClassID + "," + OpCode + "," + CustNum + ")/PartXRefVends(" + Company + "," + PartNum + "," + VendorNum + "," + VendPartNum + "," + MfgNum + "," + MfgPartNum + ")",headers=creds) as resp:
           return await resp.json()

async def get_PartXRefVends(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get PartXRefVends items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PartXRefVends
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PartXRefVendRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AprvVendSvc/PartXRefVends",headers=creds) as resp:
           return await resp.json()

async def post_PartXRefVends(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PartXRefVends
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PartXRefVendRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PartXRefVendRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AprvVendSvc/PartXRefVends", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_PartXRefVends_Company_PartNum_VendorNum_VendPartNum_MfgNum_MfgPartNum(Company, PartNum, VendorNum, VendPartNum, MfgNum, MfgPartNum, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PartXRefVend item
   Description: Calls GetByID to retrieve the PartXRefVend item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PartXRefVend
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param VendorNum: Desc: VendorNum   Required: True
      :param VendPartNum: Desc: VendPartNum   Required: True   Allow empty value : True
      :param MfgNum: Desc: MfgNum   Required: True
      :param MfgPartNum: Desc: MfgPartNum   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PartXRefVendRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AprvVendSvc/PartXRefVends(" + Company + "," + PartNum + "," + VendorNum + "," + VendPartNum + "," + MfgNum + "," + MfgPartNum + ")",headers=creds) as resp:
           return await resp.json()

async def patch_PartXRefVends_Company_PartNum_VendorNum_VendPartNum_MfgNum_MfgPartNum(Company, PartNum, VendorNum, VendPartNum, MfgNum, MfgPartNum, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update PartXRefVend for the service
   Description: Calls UpdateExt to update PartXRefVend. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PartXRefVend
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param VendorNum: Desc: VendorNum   Required: True
      :param VendPartNum: Desc: VendPartNum   Required: True   Allow empty value : True
      :param MfgNum: Desc: MfgNum   Required: True
      :param MfgPartNum: Desc: MfgPartNum   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PartXRefVendRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.AprvVendSvc/PartXRefVends(" + Company + "," + PartNum + "," + VendorNum + "," + VendPartNum + "," + MfgNum + "," + MfgPartNum + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_PartXRefVends_Company_PartNum_VendorNum_VendPartNum_MfgNum_MfgPartNum(Company, PartNum, VendorNum, VendPartNum, MfgNum, MfgPartNum, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete PartXRefVend item
   Description: Call UpdateExt to delete PartXRefVend item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PartXRefVend
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param VendorNum: Desc: VendorNum   Required: True
      :param VendPartNum: Desc: VendPartNum   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.AprvVendSvc/PartXRefVends(" + Company + "," + PartNum + "," + VendorNum + "," + VendPartNum + "," + MfgNum + "," + MfgPartNum + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.AprvVendListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AprvVendSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseAprvVend, whereClausePartXRefVend, pageSize, absolutePage, epicorHeaders = None):
   """  
   Summary: Invoke method GetRows
   Description: Returns a dataset containing all rows that satisfy the where clauses.
   OperationID: Get_GetRows
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
   params += "whereClauseAprvVend=" + whereClauseAprvVend
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClausePartXRefVend=" + whereClausePartXRefVend
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AprvVendSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(vendorNum, partNum, apVType, classID, opCode, custNum, epicorHeaders = None):
   """  
   Summary: Invoke method GetByID
   Description: Returns a DataSet given the primary key.
   OperationID: Get_GetByID
   Required: True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
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
   params += "vendorNum=" + vendorNum
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "partNum=" + partNum
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "apVType=" + apVType
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "classID=" + classID
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "opCode=" + opCode
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "custNum=" + custNum

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AprvVendSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AprvVendSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_GetAprvData(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetAprvData
   Description: .
   OperationID: GetAprvData
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetAprvData_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetAprvData_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AprvVendSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetListbyVendorName(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetListbyVendorName
   Description: Search suppliers by Vendor Name. Call normal GetList method.
   OperationID: GetListbyVendorName
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetListbyVendorName_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetListbyVendorName_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AprvVendSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_GetRowsForLandingPage(whereClauseAprvVend, whereClausePartXRefVend, VendorID, pageSize, absolutePage, epicorHeaders = None):
   """  
   Summary: Invoke method GetRowsForLandingPage
   Description: Search suppliers by Vendor Name. Method created to call from Kinetic because of incorrect/inconsistent parameter names in GetRowCustom.
   OperationID: Get_GetRowsForLandingPage
      :param whereClauseAprvVend: Desc: Where Clause for AprvVend.   Required: True   Allow empty value : True
      :param whereClausePartXRefVend: Desc: Where Clause for PartXRefVend.   Required: True   Allow empty value : True
      :param VendorID: Desc: Vendor Name.   Required: True   Allow empty value : True
      :param pageSize: Desc: Page size.   Required: True
      :param absolutePage: Desc: Absolute page.   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRowsForLandingPage_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  

   firstParam = True
   params = ""
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseAprvVend=" + whereClauseAprvVend
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClausePartXRefVend=" + whereClausePartXRefVend
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "VendorID=" + VendorID
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AprvVendSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetRowsCustom(whereClauseAprvVend, whereClausePartXRefVend, PageSize, AbsolutePage, VendorID, epicorHeaders = None):
   """  
   Summary: Invoke method GetRowsCustom
   Description: Search suppliers by Vendor Name. Call normal GetList method.
   OperationID: Get_GetRowsCustom
      :param whereClauseAprvVend: Desc: Where Clause for AprvVend.   Required: True   Allow empty value : True
      :param whereClausePartXRefVend: Desc: Where Clause for PartXRefVend.   Required: True   Allow empty value : True
      :param PageSize: Desc: Page size.   Required: True
      :param AbsolutePage: Desc: Absolute page.   Required: True
      :param VendorID: Desc: Vendor Name.   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRowsCustom_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  

   firstParam = True
   params = ""
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseAprvVend=" + whereClauseAprvVend
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClausePartXRefVend=" + whereClausePartXRefVend
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "PageSize=" + PageSize
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "AbsolutePage=" + AbsolutePage
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "VendorID=" + VendorID

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AprvVendSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeClassID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeClassID
   Description: .
   OperationID: OnChangeClassID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeClassID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeClassID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AprvVendSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeCustID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeCustID
   Description: .
   OperationID: OnChangeCustID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeCustID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeCustID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AprvVendSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeCustNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeCustNum
   Description: .
   OperationID: OnChangeCustNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeCustNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeCustNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AprvVendSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeMfgNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeMfgNum
   Description: .
   OperationID: OnChangeMfgNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeMfgNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeMfgNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AprvVendSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeMfgPartNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeMfgPartNum
   Description: .
   OperationID: OnChangeMfgPartNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeMfgPartNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeMfgPartNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AprvVendSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeOpCode(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeOpCode
   Description: .
   OperationID: OnChangeOpCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeOpCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeOpCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AprvVendSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangePartNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangePartNum
   Description: .
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AprvVendSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeVendorID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeVendorID
   Description: .
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AprvVendSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeVendorNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeVendorNum
   Description: .
   OperationID: OnChangeVendorNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeVendorNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeVendorNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AprvVendSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeVendPartNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeVendPartNum
   Description: Run when the PartXRefVend.VendPartNum is changing.
   OperationID: OnChangeVendPartNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeVendPartNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeVendPartNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AprvVendSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewAprvVend(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewAprvVend
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewAprvVend
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewAprvVend_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewAprvVend_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AprvVendSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewPartXRefVend(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewPartXRefVend
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPartXRefVend
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPartXRefVend_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPartXRefVend_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AprvVendSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AprvVendSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AprvVendSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AprvVendSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AprvVendSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AprvVendSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_AprvVendListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_AprvVendListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_AprvVendRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_AprvVendRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PartXRefVendRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PartXRefVendRow] = obj["value"]
      pass

class Erp_Tablesets_AprvVendListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.APVType:str = obj["APVType"]
      """  "MTL" Material Suppliers or "Sub" Subcontractors.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  The internal key used to tie back to the Vendor master file.  """  
      self.PartNum:str = obj["PartNum"]
      """  The PartNum field identifies the Part and is used as the primary key.  """  
      self.ClassID:str = obj["ClassID"]
      """  Inventory class. Only pertains when APVType = "MTL". The Class field can be blank or must be valid in the PartClass master file.  """  
      self.CustNum:int = obj["CustNum"]
      """  The unique key  of the Parent Customer record for the ShipTo.  """  
      self.OpCode:str = obj["OpCode"]
      """  Operation Master Code - Links record with a OpMaster record.    Only pertains when APVType = "Sub".  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.APVTypeX:str = obj["APVTypeX"]
      """  APVTypeX  """  
      self.CalledFrom:str = obj["CalledFrom"]
      self.ClassIDDescription:str = obj["ClassIDDescription"]
      """  Full description of the part class.  """  
      self.CustNumBTName:str = obj["CustNumBTName"]
      """  The Bill To name of this customer. Will be used by the AR module for Invoices. This defaults to the Customer.Name but can be overrode by the user.  """  
      self.CustNumCustID:str = obj["CustNumCustID"]
      """  A user defined external customer ID.  This must be unique within the file.  This ID may be used in certain screen displays or reports where a full customer name is inappropriate. Therefore users should use meaningful characters as they would in any other master file. This master file key is a little different in that the user can change. This change is allowed because the system is not using the CustID as a foreign key in any other file.  Rather it uses the CustNum field which is assigned to th  """  
      self.CustNumName:str = obj["CustNumName"]
      """  The full name of the customer.  """  
      self.OpCodeOpDesc:str = obj["OpCodeOpDesc"]
      """  Description of the operation.  Job, BOM, and Quote entry use this as a default description when entering operation details.  """  
      self.PartNumPartDescription:str = obj["PartNumPartDescription"]
      """  Describes the Part.  """  
      self.PartNumSellingFactor:int = obj["PartNumSellingFactor"]
      """   This value is used to convert quantity when there is a difference in the customers unit of measure and how it is stocked in inventory. Example is sold in pounds, stocked in sheets.  

Formula: Inventory Qty * Conversion Factor = Selling Qty.  """  
      self.PartNumTrackSerialNum:bool = obj["PartNumTrackSerialNum"]
      """  Indicates if this part is serial number tracked  """  
      self.PartNumPricePerCode:str = obj["PartNumPricePerCode"]
      """  Indicates the pricing per quantity for this part. It can be "E" = per each, "C" = per hundred,  "M" = per thousand. Maintainable only via Part Maintenance. The initial default is "E". Used as default PricePerCode in order entry and invoice entry.  """  
      self.PartNumTrackDimension:bool = obj["PartNumTrackDimension"]
      """   Onhand quantity is always tracked in the Parts primary inventory uom (Part.IUM). Checking this box indicates that you want to allow tracking of onhand quantity by additional uoms. 
The actual UOMs to be tracked for the part are indicated by PartUOM.TrackOnHand. In order to set the PartUOM.TrackOhHand = True the Part.TrackDimension must = true.
This replaces the old 8.3 Track Dimension feature  """  
      self.PartNumIUM:str = obj["PartNumIUM"]
      """  Primary Inventory Unit of Measure. The unit costs, are based on this uom. Used as a default for issue transactions for the part.  Part onhand and allocation quantities are tracked by this uom.  The quantities can also be tracked by other uoms (see PartUOM table) but tracking at this uom is mandatory.   Use UOMClass.DefUOMCode of the system default UOMClass  when creating new part records (see XASyst.DefUOMClassID).  """  
      self.PartNumSalesUM:str = obj["PartNumSalesUM"]
      """  The Selling Unit of measure for the Part. The UOM which the unit prices are based on. Defaults as the Part.IUM.  """  
      self.PartNumTrackLots:bool = obj["PartNumTrackLots"]
      """  Indicates if Lot numbers are prompted for in transactions for this part.  Backflushing and AutoReceiving functions are ignored when TrackLots = Yes.  """  
      self.VendorNumAddress3:str = obj["VendorNumAddress3"]
      """  Third address line of the Supplier  """  
      self.VendorNumCurrencyCode:str = obj["VendorNumCurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.VendorNumZIP:str = obj["VendorNumZIP"]
      """  Postal Code or Zip code portion of the address of the Supplier  """  
      self.VendorNumState:str = obj["VendorNumState"]
      """  Can be blank.  """  
      self.VendorNumAddress1:str = obj["VendorNumAddress1"]
      """  First address line of the Supplier  """  
      self.VendorNumCity:str = obj["VendorNumCity"]
      """  City portion of the address of the Supplier  """  
      self.VendorNumDefaultFOB:str = obj["VendorNumDefaultFOB"]
      """  Default FOB policy for Purchase Orders to this vendor.  Used as a default to POHeader.FOB.  """  
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
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_AprvVendRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.APVType:str = obj["APVType"]
      """  "MTL" Material Suppliers or "Sub" Subcontractors.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  The internal key used to tie back to the Vendor master file.  """  
      self.PartNum:str = obj["PartNum"]
      """  The PartNum field identifies the Part and is used as the primary key.  """  
      self.ClassID:str = obj["ClassID"]
      """  Inventory class. Only pertains when APVType = "MTL". The Class field can be blank or must be valid in the PartClass master file.  """  
      self.CustNum:int = obj["CustNum"]
      """  The unique key  of the Parent Customer record for the ShipTo.  """  
      self.OpCode:str = obj["OpCode"]
      """  Operation Master Code - Links record with a OpMaster record.    Only pertains when APVType = "Sub".  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.APVTypeX:str = obj["APVTypeX"]
      """  APVTypeX  """  
      self.CalledFrom:str = obj["CalledFrom"]
      self.BitFlag:int = obj["BitFlag"]
      self.ClassIDDescription:str = obj["ClassIDDescription"]
      self.CustNumBTName:str = obj["CustNumBTName"]
      self.CustNumCustID:str = obj["CustNumCustID"]
      self.CustNumName:str = obj["CustNumName"]
      self.OpCodeOpDesc:str = obj["OpCodeOpDesc"]
      self.PartNumSellingFactor:int = obj["PartNumSellingFactor"]
      self.PartNumPricePerCode:str = obj["PartNumPricePerCode"]
      self.PartNumIUM:str = obj["PartNumIUM"]
      self.PartNumTrackSerialNum:bool = obj["PartNumTrackSerialNum"]
      self.PartNumSalesUM:str = obj["PartNumSalesUM"]
      self.PartNumTrackLots:bool = obj["PartNumTrackLots"]
      self.PartNumPartDescription:str = obj["PartNumPartDescription"]
      self.PartNumTrackDimension:bool = obj["PartNumTrackDimension"]
      self.VendorNumAddress3:str = obj["VendorNumAddress3"]
      self.VendorNumAddress2:str = obj["VendorNumAddress2"]
      self.VendorNumCountry:str = obj["VendorNumCountry"]
      self.VendorNumVendorID:str = obj["VendorNumVendorID"]
      self.VendorNumAddress1:str = obj["VendorNumAddress1"]
      self.VendorNumName:str = obj["VendorNumName"]
      self.VendorNumState:str = obj["VendorNumState"]
      self.VendorNumDefaultFOB:str = obj["VendorNumDefaultFOB"]
      self.VendorNumCurrencyCode:str = obj["VendorNumCurrencyCode"]
      self.VendorNumTermsCode:str = obj["VendorNumTermsCode"]
      self.VendorNumZIP:str = obj["VendorNumZIP"]
      self.VendorNumCity:str = obj["VendorNumCity"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PartXRefVendRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.PartNum:str = obj["PartNum"]
      """  PartNum  """  
      self.VendorNum:int = obj["VendorNum"]
      """  VendNum  """  
      self.VendPartNum:str = obj["VendPartNum"]
      """  VendPartNum  """  
      self.MfgNum:int = obj["MfgNum"]
      """  MfgNum  """  
      self.MfgPartNum:str = obj["MfgPartNum"]
      """  MfgPartNum  """  
      self.Reference:str = obj["Reference"]
      """  Reference  """  
      self.LeadTime:int = obj["LeadTime"]
      """  LeadTime - This LeadTime will be used if a record is present, otherwise the LeadTime on VendPart will be used.  """  
      self.PurchaseDefault:bool = obj["PurchaseDefault"]
      """  PurchaseDefault - True if this is the default. If there is at least one PartXRefVend record related to the VendPart, exactly one of these should have this field marked true.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.APVType:str = obj["APVType"]
      """  Used to mantain relation with AprvVend.  """  
      self.CustNum:int = obj["CustNum"]
      """  Used to mantain relation with AprvVend.  """  
      self.ClassID:str = obj["ClassID"]
      """  Used to mantain relation with AprvVend.  """  
      self.OpCode:str = obj["OpCode"]
      """  Used to mantain relation with AprvVend.  """  
      self.Description:str = obj["Description"]
      """  Lifecycle status description  """  
      self.BitFlag:int = obj["BitFlag"]
      self.MfgNumName:str = obj["MfgNumName"]
      self.MfgNumMfgID:str = obj["MfgNumMfgID"]
      self.MfgPartNumLifecycleStatus:str = obj["MfgPartNumLifecycleStatus"]
      self.MfgPartNumLeadTime:str = obj["MfgPartNumLeadTime"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class DeleteByID_input:
   """ Required : 
   vendorNum
   partNum
   apVType
   classID
   opCode
   custNum
   """  
   def __init__(self, obj):
      self.vendorNum:int = obj["vendorNum"]
      self.partNum:str = obj["partNum"]
      self.apVType:str = obj["apVType"]
      self.classID:str = obj["classID"]
      self.opCode:str = obj["opCode"]
      self.custNum:int = obj["custNum"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_AprvVendListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.APVType:str = obj["APVType"]
      """  "MTL" Material Suppliers or "Sub" Subcontractors.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  The internal key used to tie back to the Vendor master file.  """  
      self.PartNum:str = obj["PartNum"]
      """  The PartNum field identifies the Part and is used as the primary key.  """  
      self.ClassID:str = obj["ClassID"]
      """  Inventory class. Only pertains when APVType = "MTL". The Class field can be blank or must be valid in the PartClass master file.  """  
      self.CustNum:int = obj["CustNum"]
      """  The unique key  of the Parent Customer record for the ShipTo.  """  
      self.OpCode:str = obj["OpCode"]
      """  Operation Master Code - Links record with a OpMaster record.    Only pertains when APVType = "Sub".  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.APVTypeX:str = obj["APVTypeX"]
      """  APVTypeX  """  
      self.CalledFrom:str = obj["CalledFrom"]
      self.ClassIDDescription:str = obj["ClassIDDescription"]
      """  Full description of the part class.  """  
      self.CustNumBTName:str = obj["CustNumBTName"]
      """  The Bill To name of this customer. Will be used by the AR module for Invoices. This defaults to the Customer.Name but can be overrode by the user.  """  
      self.CustNumCustID:str = obj["CustNumCustID"]
      """  A user defined external customer ID.  This must be unique within the file.  This ID may be used in certain screen displays or reports where a full customer name is inappropriate. Therefore users should use meaningful characters as they would in any other master file. This master file key is a little different in that the user can change. This change is allowed because the system is not using the CustID as a foreign key in any other file.  Rather it uses the CustNum field which is assigned to th  """  
      self.CustNumName:str = obj["CustNumName"]
      """  The full name of the customer.  """  
      self.OpCodeOpDesc:str = obj["OpCodeOpDesc"]
      """  Description of the operation.  Job, BOM, and Quote entry use this as a default description when entering operation details.  """  
      self.PartNumPartDescription:str = obj["PartNumPartDescription"]
      """  Describes the Part.  """  
      self.PartNumSellingFactor:int = obj["PartNumSellingFactor"]
      """   This value is used to convert quantity when there is a difference in the customers unit of measure and how it is stocked in inventory. Example is sold in pounds, stocked in sheets.  

Formula: Inventory Qty * Conversion Factor = Selling Qty.  """  
      self.PartNumTrackSerialNum:bool = obj["PartNumTrackSerialNum"]
      """  Indicates if this part is serial number tracked  """  
      self.PartNumPricePerCode:str = obj["PartNumPricePerCode"]
      """  Indicates the pricing per quantity for this part. It can be "E" = per each, "C" = per hundred,  "M" = per thousand. Maintainable only via Part Maintenance. The initial default is "E". Used as default PricePerCode in order entry and invoice entry.  """  
      self.PartNumTrackDimension:bool = obj["PartNumTrackDimension"]
      """   Onhand quantity is always tracked in the Parts primary inventory uom (Part.IUM). Checking this box indicates that you want to allow tracking of onhand quantity by additional uoms. 
The actual UOMs to be tracked for the part are indicated by PartUOM.TrackOnHand. In order to set the PartUOM.TrackOhHand = True the Part.TrackDimension must = true.
This replaces the old 8.3 Track Dimension feature  """  
      self.PartNumIUM:str = obj["PartNumIUM"]
      """  Primary Inventory Unit of Measure. The unit costs, are based on this uom. Used as a default for issue transactions for the part.  Part onhand and allocation quantities are tracked by this uom.  The quantities can also be tracked by other uoms (see PartUOM table) but tracking at this uom is mandatory.   Use UOMClass.DefUOMCode of the system default UOMClass  when creating new part records (see XASyst.DefUOMClassID).  """  
      self.PartNumSalesUM:str = obj["PartNumSalesUM"]
      """  The Selling Unit of measure for the Part. The UOM which the unit prices are based on. Defaults as the Part.IUM.  """  
      self.PartNumTrackLots:bool = obj["PartNumTrackLots"]
      """  Indicates if Lot numbers are prompted for in transactions for this part.  Backflushing and AutoReceiving functions are ignored when TrackLots = Yes.  """  
      self.VendorNumAddress3:str = obj["VendorNumAddress3"]
      """  Third address line of the Supplier  """  
      self.VendorNumCurrencyCode:str = obj["VendorNumCurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.VendorNumZIP:str = obj["VendorNumZIP"]
      """  Postal Code or Zip code portion of the address of the Supplier  """  
      self.VendorNumState:str = obj["VendorNumState"]
      """  Can be blank.  """  
      self.VendorNumAddress1:str = obj["VendorNumAddress1"]
      """  First address line of the Supplier  """  
      self.VendorNumCity:str = obj["VendorNumCity"]
      """  City portion of the address of the Supplier  """  
      self.VendorNumDefaultFOB:str = obj["VendorNumDefaultFOB"]
      """  Default FOB policy for Purchase Orders to this vendor.  Used as a default to POHeader.FOB.  """  
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
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_AprvVendListTableset:
   def __init__(self, obj):
      self.AprvVendList:list[Erp_Tablesets_AprvVendListRow] = obj["AprvVendList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_AprvVendRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.APVType:str = obj["APVType"]
      """  "MTL" Material Suppliers or "Sub" Subcontractors.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  The internal key used to tie back to the Vendor master file.  """  
      self.PartNum:str = obj["PartNum"]
      """  The PartNum field identifies the Part and is used as the primary key.  """  
      self.ClassID:str = obj["ClassID"]
      """  Inventory class. Only pertains when APVType = "MTL". The Class field can be blank or must be valid in the PartClass master file.  """  
      self.CustNum:int = obj["CustNum"]
      """  The unique key  of the Parent Customer record for the ShipTo.  """  
      self.OpCode:str = obj["OpCode"]
      """  Operation Master Code - Links record with a OpMaster record.    Only pertains when APVType = "Sub".  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.APVTypeX:str = obj["APVTypeX"]
      """  APVTypeX  """  
      self.CalledFrom:str = obj["CalledFrom"]
      self.BitFlag:int = obj["BitFlag"]
      self.ClassIDDescription:str = obj["ClassIDDescription"]
      self.CustNumBTName:str = obj["CustNumBTName"]
      self.CustNumCustID:str = obj["CustNumCustID"]
      self.CustNumName:str = obj["CustNumName"]
      self.OpCodeOpDesc:str = obj["OpCodeOpDesc"]
      self.PartNumSellingFactor:int = obj["PartNumSellingFactor"]
      self.PartNumPricePerCode:str = obj["PartNumPricePerCode"]
      self.PartNumIUM:str = obj["PartNumIUM"]
      self.PartNumTrackSerialNum:bool = obj["PartNumTrackSerialNum"]
      self.PartNumSalesUM:str = obj["PartNumSalesUM"]
      self.PartNumTrackLots:bool = obj["PartNumTrackLots"]
      self.PartNumPartDescription:str = obj["PartNumPartDescription"]
      self.PartNumTrackDimension:bool = obj["PartNumTrackDimension"]
      self.VendorNumAddress3:str = obj["VendorNumAddress3"]
      self.VendorNumAddress2:str = obj["VendorNumAddress2"]
      self.VendorNumCountry:str = obj["VendorNumCountry"]
      self.VendorNumVendorID:str = obj["VendorNumVendorID"]
      self.VendorNumAddress1:str = obj["VendorNumAddress1"]
      self.VendorNumName:str = obj["VendorNumName"]
      self.VendorNumState:str = obj["VendorNumState"]
      self.VendorNumDefaultFOB:str = obj["VendorNumDefaultFOB"]
      self.VendorNumCurrencyCode:str = obj["VendorNumCurrencyCode"]
      self.VendorNumTermsCode:str = obj["VendorNumTermsCode"]
      self.VendorNumZIP:str = obj["VendorNumZIP"]
      self.VendorNumCity:str = obj["VendorNumCity"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_AprvVendTableset:
   def __init__(self, obj):
      self.AprvVend:list[Erp_Tablesets_AprvVendRow] = obj["AprvVend"]
      self.PartXRefVend:list[Erp_Tablesets_PartXRefVendRow] = obj["PartXRefVend"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_PartXRefVendRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.PartNum:str = obj["PartNum"]
      """  PartNum  """  
      self.VendorNum:int = obj["VendorNum"]
      """  VendNum  """  
      self.VendPartNum:str = obj["VendPartNum"]
      """  VendPartNum  """  
      self.MfgNum:int = obj["MfgNum"]
      """  MfgNum  """  
      self.MfgPartNum:str = obj["MfgPartNum"]
      """  MfgPartNum  """  
      self.Reference:str = obj["Reference"]
      """  Reference  """  
      self.LeadTime:int = obj["LeadTime"]
      """  LeadTime - This LeadTime will be used if a record is present, otherwise the LeadTime on VendPart will be used.  """  
      self.PurchaseDefault:bool = obj["PurchaseDefault"]
      """  PurchaseDefault - True if this is the default. If there is at least one PartXRefVend record related to the VendPart, exactly one of these should have this field marked true.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.APVType:str = obj["APVType"]
      """  Used to mantain relation with AprvVend.  """  
      self.CustNum:int = obj["CustNum"]
      """  Used to mantain relation with AprvVend.  """  
      self.ClassID:str = obj["ClassID"]
      """  Used to mantain relation with AprvVend.  """  
      self.OpCode:str = obj["OpCode"]
      """  Used to mantain relation with AprvVend.  """  
      self.Description:str = obj["Description"]
      """  Lifecycle status description  """  
      self.BitFlag:int = obj["BitFlag"]
      self.MfgNumName:str = obj["MfgNumName"]
      self.MfgNumMfgID:str = obj["MfgNumMfgID"]
      self.MfgPartNumLifecycleStatus:str = obj["MfgPartNumLifecycleStatus"]
      self.MfgPartNumLeadTime:str = obj["MfgPartNumLeadTime"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_UpdExtAprvVendTableset:
   def __init__(self, obj):
      self.AprvVend:list[Erp_Tablesets_AprvVendRow] = obj["AprvVend"]
      self.PartXRefVend:list[Erp_Tablesets_PartXRefVendRow] = obj["PartXRefVend"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetAprvData_input:
   """ Required : 
   ipCalledFrom
   whereClauze
   """  
   def __init__(self, obj):
      self.ipCalledFrom:str = obj["ipCalledFrom"]
      """  Called From  """  
      self.whereClauze:str = obj["whereClauze"]
      """  WhereClauze  """  
      pass

class GetAprvData_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_AprvVendTableset] = obj["returnObj"]
      pass

class GetByID_input:
   """ Required : 
   vendorNum
   partNum
   apVType
   classID
   opCode
   custNum
   """  
   def __init__(self, obj):
      self.vendorNum:int = obj["vendorNum"]
      self.partNum:str = obj["partNum"]
      self.apVType:str = obj["apVType"]
      self.classID:str = obj["classID"]
      self.opCode:str = obj["opCode"]
      self.custNum:int = obj["custNum"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_AprvVendTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_AprvVendTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_AprvVendTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_AprvVendListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetListbyVendorName_input:
   """ Required : 
   WhereClause
   PageSize
   AbsolutePage
   VendorName
   """  
   def __init__(self, obj):
      self.WhereClause:str = obj["WhereClause"]
      """  Whereclause.  """  
      self.PageSize:int = obj["PageSize"]
      """  Page size.  """  
      self.AbsolutePage:int = obj["AbsolutePage"]
      """  Absolute page.  """  
      self.VendorName:str = obj["VendorName"]
      """  Vendor Name.  """  
      pass

class GetListbyVendorName_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_AprvVendListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.MorePages:bool = obj["MorePages"]
      pass

      """  output parameters  """  

class GetNewAprvVend_input:
   """ Required : 
   ds
   vendorNum
   partNum
   apVType
   classID
   opCode
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_AprvVendTableset] = obj["ds"]
      self.vendorNum:int = obj["vendorNum"]
      self.partNum:str = obj["partNum"]
      self.apVType:str = obj["apVType"]
      self.classID:str = obj["classID"]
      self.opCode:str = obj["opCode"]
      pass

class GetNewAprvVend_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_AprvVendTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewPartXRefVend_input:
   """ Required : 
   ds
   partNum
   vendorNum
   vendPartNum
   mfgNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_AprvVendTableset] = obj["ds"]
      self.partNum:str = obj["partNum"]
      self.vendorNum:int = obj["vendorNum"]
      self.vendPartNum:str = obj["vendPartNum"]
      self.mfgNum:int = obj["mfgNum"]
      pass

class GetNewPartXRefVend_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_AprvVendTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRowsCustom_input:
   """ Required : 
   whereClauseAprvVend
   whereClausePartXRefVend
   PageSize
   AbsolutePage
   VendorID
   """  
   def __init__(self, obj):
      self.whereClauseAprvVend:str = obj["whereClauseAprvVend"]
      """  Where Clause for AprvVend.  """  
      self.whereClausePartXRefVend:str = obj["whereClausePartXRefVend"]
      """  Where Clause for PartXRefVend.  """  
      self.PageSize:int = obj["PageSize"]
      """  Page size.  """  
      self.AbsolutePage:int = obj["AbsolutePage"]
      """  Absolute page.  """  
      self.VendorID:str = obj["VendorID"]
      """  Vendor Name.  """  
      pass

class GetRowsCustom_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_AprvVendTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.MorePages:bool = obj["MorePages"]
      pass

      """  output parameters  """  

class GetRowsForLandingPage_input:
   """ Required : 
   whereClauseAprvVend
   whereClausePartXRefVend
   VendorID
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseAprvVend:str = obj["whereClauseAprvVend"]
      """  Where Clause for AprvVend.  """  
      self.whereClausePartXRefVend:str = obj["whereClausePartXRefVend"]
      """  Where Clause for PartXRefVend.  """  
      self.VendorID:str = obj["VendorID"]
      """  Vendor Name.  """  
      self.pageSize:int = obj["pageSize"]
      """  Page size.  """  
      self.absolutePage:int = obj["absolutePage"]
      """  Absolute page.  """  
      pass

class GetRowsForLandingPage_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_AprvVendTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseAprvVend
   whereClausePartXRefVend
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseAprvVend:str = obj["whereClauseAprvVend"]
      self.whereClausePartXRefVend:str = obj["whereClausePartXRefVend"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_AprvVendTableset] = obj["returnObj"]
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

class OnChangeClassID_input:
   """ Required : 
   ipClassID
   ds
   """  
   def __init__(self, obj):
      self.ipClassID:str = obj["ipClassID"]
      """  The new value for VendorID.  """  
      self.ds:list[Erp_Tablesets_AprvVendTableset] = obj["ds"]
      pass

class OnChangeClassID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_AprvVendTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeCustID_input:
   """ Required : 
   ipCustID
   ds
   """  
   def __init__(self, obj):
      self.ipCustID:str = obj["ipCustID"]
      """  The new value for VendorID.  """  
      self.ds:list[Erp_Tablesets_AprvVendTableset] = obj["ds"]
      pass

class OnChangeCustID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_AprvVendTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeCustNum_input:
   """ Required : 
   ipCustNum
   ds
   """  
   def __init__(self, obj):
      self.ipCustNum:int = obj["ipCustNum"]
      """  The new value for VendorID.  """  
      self.ds:list[Erp_Tablesets_AprvVendTableset] = obj["ds"]
      pass

class OnChangeCustNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_AprvVendTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeMfgNum_input:
   """ Required : 
   ipMfgNum
   ds
   """  
   def __init__(self, obj):
      self.ipMfgNum:int = obj["ipMfgNum"]
      """  The new value for VendorID.  """  
      self.ds:list[Erp_Tablesets_AprvVendTableset] = obj["ds"]
      pass

class OnChangeMfgNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_AprvVendTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeMfgPartNum_input:
   """ Required : 
   ipMfgPartNum
   ds
   """  
   def __init__(self, obj):
      self.ipMfgPartNum:str = obj["ipMfgPartNum"]
      """  The new value for VendorID.  """  
      self.ds:list[Erp_Tablesets_AprvVendTableset] = obj["ds"]
      pass

class OnChangeMfgPartNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_AprvVendTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeOpCode_input:
   """ Required : 
   ipOpCode
   ds
   """  
   def __init__(self, obj):
      self.ipOpCode:str = obj["ipOpCode"]
      """  The new value for VendorID.  """  
      self.ds:list[Erp_Tablesets_AprvVendTableset] = obj["ds"]
      pass

class OnChangeOpCode_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_AprvVendTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangePartNum_input:
   """ Required : 
   ipPartNum
   ds
   """  
   def __init__(self, obj):
      self.ipPartNum:str = obj["ipPartNum"]
      """  The new value for VendorID.  """  
      self.ds:list[Erp_Tablesets_AprvVendTableset] = obj["ds"]
      pass

class OnChangePartNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_AprvVendTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeVendPartNum_input:
   """ Required : 
   ipVendPartNum
   ds
   """  
   def __init__(self, obj):
      self.ipVendPartNum:str = obj["ipVendPartNum"]
      """  The new value for VendPartNum.  """  
      self.ds:list[Erp_Tablesets_AprvVendTableset] = obj["ds"]
      pass

class OnChangeVendPartNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_AprvVendTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeVendorID_input:
   """ Required : 
   ipVendorID
   ds
   """  
   def __init__(self, obj):
      self.ipVendorID:str = obj["ipVendorID"]
      """  The new value for VendorID.  """  
      self.ds:list[Erp_Tablesets_AprvVendTableset] = obj["ds"]
      pass

class OnChangeVendorID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_AprvVendTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeVendorNum_input:
   """ Required : 
   ipVendorNum
   ds
   """  
   def __init__(self, obj):
      self.ipVendorNum:int = obj["ipVendorNum"]
      """  The new value for VendorID.  """  
      self.ds:list[Erp_Tablesets_AprvVendTableset] = obj["ds"]
      pass

class OnChangeVendorNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_AprvVendTableset] = obj["ds"]
      pass

      """  output parameters  """  

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtAprvVendTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtAprvVendTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_AprvVendTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_AprvVendTableset] = obj["ds"]
      pass

      """  output parameters  """  

